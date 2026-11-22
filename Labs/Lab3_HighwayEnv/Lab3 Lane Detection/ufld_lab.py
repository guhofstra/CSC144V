"""
ufld_lab.py -- helper module for CSC144V Lab3 (lane detection with UFLD v1).

Wraps the pretrained Ultra-Fast-Lane-Detection (v1, ResNet-18) model from
https://github.com/cfzd/Ultra-Fast-Lane-Detection (MIT license) so that it can be run
on ANY image / video frame and on CPU or GPU, and so that gradients can flow back to
the input image (needed for the adversarial attacks in Task 3).

You do NOT need to modify this file. Tasks 2 and 3 are implemented in the notebook.

Key facts about UFLD v1 (read this before Task 3!)
--------------------------------------------------
* Input : RGB image resized to 288 x 800 (H x W), ImageNet-normalised.
* Output: tensor `logits` of shape (1, G+1, A, 4)
              G = number of grid columns (TuSimple: 100, CULane: 200)
              A = number of row anchors  (TuSimple: 56,  CULane: 18)
              4 = max number of lanes    (slots, ordered left -> right)
  For every (row anchor a, lane slot l) the network does a (G+1)-way classification:
  "which of the G grid columns contains lane l on row a?" -- class G means "no lane here".
* Lane detection is therefore a CLASSIFICATION problem, so cross-entropy + FGSM/PGD
  (Lab1) apply almost unchanged.
"""
import os
import sys
import warnings

import cv2
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image

# Row anchors (y positions in the 288-pixel-high network input), copied from data/constant.py of the UFLD repo.
TUSIMPLE_ROW_ANCHOR = list(range(64, 285, 4))  # 56 anchors: 64, 68, ..., 284
CULANE_ROW_ANCHOR = [121, 131, 141, 150, 160, 170, 180, 189, 199, 209, 219, 228, 238, 248, 258, 267, 277, 287]

DATASETS = {
    "Tusimple": dict(griding_num=100, num_anchors=56, row_anchor=TUSIMPLE_ROW_ANCHOR, img_w=1280, img_h=720),
    "CULane": dict(griding_num=200, num_anchors=18, row_anchor=CULANE_ROW_ANCHOR, img_w=1640, img_h=590),
}
NET_H, NET_W = 288, 800
NUM_LANES = 4


class LaneDetector:
    """Pretrained UFLD v1 (ResNet-18) with a differentiable forward pass.

    repo_dir : path of the cloned Ultra-Fast-Lane-Detection repository
    weights  : path of tusimple_18.pth / culane_18.pth (None -> random weights, for code tests only)
    dataset  : 'Tusimple' or 'CULane' (must match the weights!)
    """

    def __init__(self, repo_dir, weights, dataset="Tusimple", device=None):
        repo_dir = os.path.abspath(repo_dir)
        if repo_dir not in sys.path:
            sys.path.insert(0, repo_dir)
        from model.model import parsingNet  # from the UFLD repo

        cfg = DATASETS[dataset]
        self.dataset = dataset
        self.G = cfg["griding_num"]
        self.A = cfg["num_anchors"]
        self.row_anchor = cfg["row_anchor"]
        self.default_size = (cfg["img_w"], cfg["img_h"])
        self.device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))

        self.net = parsingNet(pretrained=False, backbone="18",
                              cls_dim=(self.G + 1, self.A, NUM_LANES), use_aux=False)
        if weights is not None:
            try:
                ckpt = torch.load(weights, map_location="cpu")
            except Exception:  # older checkpoints may need weights_only=False (trusted course weights only)
                ckpt = torch.load(weights, map_location="cpu", weights_only=False)
            sd = ckpt["model"] if "model" in ckpt else ckpt
            sd = {(k[7:] if k.startswith("module.") else k): v for k, v in sd.items()}
            res = self.net.load_state_dict(sd, strict=False)  # aux_* keys are not needed at test time
            if res.missing_keys:
                warnings.warn(f"missing keys when loading weights (wrong dataset/weights?): {res.missing_keys[:5]}")
        self.net.to(self.device).eval()
        for p in self.net.parameters():
            p.requires_grad_(False)  # we only need gradients w.r.t. the INPUT image
        self.mean = torch.tensor([0.485, 0.456, 0.406], device=self.device).view(1, 3, 1, 1)
        self.std = torch.tensor([0.229, 0.224, 0.225], device=self.device).view(1, 3, 1, 1)

    # ------------------------------------------------------------------ pre-processing
    def to_tensor(self, img_bgr):
        """BGR uint8 image (any size) -> float tensor (1,3,288,800) with values in [0,1] (NOT normalised)."""
        rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        pil = Image.fromarray(rgb).resize((NET_W, NET_H), Image.BILINEAR)
        x = torch.from_numpy(np.asarray(pil).copy()).permute(2, 0, 1).float().div(255.0).unsqueeze(0)
        # .contiguous(): the permuted tensor is channels_last; the UFLD head uses .view() and needs NCHW-contiguous
        return x.contiguous().to(self.device)

    @staticmethod
    def to_bgr(x01):
        """(1,3,288,800) tensor in [0,1] -> BGR uint8 image of size 288x800 (for display / saving)."""
        a = (x01[0].detach().clamp(0, 1).permute(1, 2, 0).cpu().numpy() * 255.0).round().astype(np.uint8)
        return cv2.cvtColor(a, cv2.COLOR_RGB2BGR)

    # ------------------------------------------------------------------ network
    def forward(self, x01):
        """Differentiable forward pass. x01: (N,3,288,800) in [0,1]. Returns logits (N, G+1, A, 4)."""
        return self.net(((x01 - self.mean) / self.std).contiguous())

    @torch.no_grad()
    def logits(self, x01):
        return self.forward(x01)

    # ------------------------------------------------------------------ post-processing
    def decode(self, logits, img_w, img_h):
        """logits -> list of 4 arrays (one per lane slot, left->right), each of shape (n,2) with (x,y) pixel
        coordinates in an image of size img_w x img_h. A slot with <= 2 points is returned as an empty (0,2) array.
        Same post-processing as demo.py of the UFLD repo (soft-argmax over the grid columns)."""
        G, A = self.G, self.A
        out = logits[0].detach().float().cpu().numpy()[:, ::-1, :]  # flip rows: k=0 is the bottom-most anchor
        e = np.exp(out[:-1] - out[:-1].max(axis=0, keepdims=True))
        prob = e / e.sum(axis=0, keepdims=True)
        idx = (np.arange(G) + 1).reshape(-1, 1, 1)
        loc = (prob * idx).sum(axis=0)  # (A, 4) expected grid index (1-based)
        loc[out.argmax(axis=0) == G] = 0  # class G = "no lane"
        col_w = (NET_W - 1) / (G - 1)  # width of one grid cell in the 800-px network input
        lanes = []
        for i in range(NUM_LANES):
            if (loc[:, i] != 0).sum() > 2:
                pts = [(loc[k, i] * col_w * img_w / NET_W - 1, img_h * (self.row_anchor[A - 1 - k] / NET_H) - 1)
                       for k in range(A) if loc[k, i] > 0]
                lanes.append(np.asarray(pts, dtype=np.float32))
            else:
                lanes.append(np.zeros((0, 2), dtype=np.float32))
        return lanes

    def cell_width_px(self, img_w=NET_W):
        """Width of ONE grid cell in pixels of an image that is img_w wide (useful for interpreting shifts)."""
        return (NET_W - 1) / (self.G - 1) * img_w / NET_W

    def detect(self, img_bgr):
        """Convenience: image -> (lanes in ORIGINAL image coordinates, logits)."""
        h, w = img_bgr.shape[:2]
        lg = self.logits(self.to_tensor(img_bgr))
        return self.decode(lg, w, h), lg

    def lanes_at_net_res(self, logits):
        """Decode in the 800x288 coordinate system of the network input (used for adversarial examples)."""
        return self.decode(logits, NET_W, NET_H)


# ---------------------------------------------------------------------- visualisation / IO helpers
LANE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]  # BGR; slot 0..3


def draw_lanes(img_bgr, lanes, radius=4, colors=LANE_COLORS):
    out = img_bgr.copy()
    for i, pts in enumerate(lanes):
        for x, y in pts:
            cv2.circle(out, (int(round(x)), int(round(y))), radius, colors[i % len(colors)], -1)
    return out


def video_frames(path, stride=1, max_frames=None):
    """Yield (frame_index, BGR frame) from a video file, taking every `stride`-th frame."""
    cap = cv2.VideoCapture(path)
    i = n = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if i % stride == 0:
            yield i, frame
            n += 1
            if max_frames is not None and n >= max_frames:
                break
        i += 1
    cap.release()


def cell_stats(det, logits_clean, logits_adv):
    """Cell-level effect of an attack, computed on the lane cells the CLEAN model predicted.
    Returns a dict with
      changed : fraction of lane cells whose predicted grid column changed (any change, incl. 'no lane')
      mean_shift_cells : mean signed change of the grid column (adv - clean) over cells that are still lane cells
      mean_shift_px : the same in pixels of the 800-px-wide network input
    """
    G = det.G
    pc, pa = logits_clean.argmax(1), logits_adv.argmax(1)  # (N, A, 4)
    valid = pc < G
    if valid.sum() == 0:
        return dict(changed=float("nan"), mean_shift_cells=float("nan"), mean_shift_px=float("nan"))
    changed = (pa != pc)[valid].float().mean().item()
    still = valid & (pa < G)
    shift = (pa - pc)[still].float().mean().item() if still.sum() > 0 else float("nan")
    return dict(changed=changed, mean_shift_cells=shift, mean_shift_px=shift * det.cell_width_px(NET_W))
