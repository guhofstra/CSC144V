# 审计日志：L4 Object Detection and Segmentation.pptx

日期：2026-10-07　范围：内容错误 + 更新审计（只改 run 文本，不增删页、不改版式/图片）

## 摘要
- 共 19 处文本编辑（run 级），涉及 15 张幻灯片的正文 + 1 处备注（S45 备注）；幻灯片数 49 → 49（未变）。
- 实质性技术错误 4 项：S14 滑窗总数量级（57 million → 约 58 billion）、S37 Panoptic 定义（thing → stuff）、S20/S25 Fast R-CNN 的 Selective Search 作用对象、S45 备注 bicubic 邻域数。
- 其余为占位符/拼写/术语一致性（S10 "??"、S24 Girshick、S7 IoU 写法等）。
- 更新审计：本讲义无具体"最新模型/榜单数字"，唯一过时的论断是 S35（见"待你确认"）；未改。
- 备份：`bak/audit-20261007/` 未动。未发现 `~$` 锁文件（PowerPoint 未打开该文件）。
- 写回校验：磁盘文件 md5 = 77236475ba70f593b5791c33b4dc0249，大小 19,179,847 B，python-pptx 读到 49 页。

## 修改清单
| 幻灯片 | 修改前 → 修改后 | 原因 | 来源 |
|---|---|---|---|
| S4 | `predict ”what” (class label)` → `predict “what” (class label)` | 开引号方向写反 | — |
| S7 | 标题 `IOU)` → `IoU)`；公式内 `IOU` → `IoU` | 全讲义（S8–S12）统一用 IoU | — |
| S8 | `Discard (suppresses) overlapping` → `Discard (suppress) overlapping` | 语法 | — |
| S9 | `IoU > thresh, mark it as TP` → `IoU ≥ thresh, ...` | 与 S7（≥θ）和 S12（≥ threshold）一致；COCO 定义为 ≥ | — |
| S10 | `correct ??% of the time` → `correct X% of the time`；`classifies ??% of them` → `classifies X% of them` | 占位符 `??`（若是故意留空，见待确认） | — |
| S10 | `the classier correctly` → `the classifier correctly` | 拼写 | — |
| S14 | `For an 800x600 image, that is 57 million!` → `that is about 58 billion!` | 按本页公式 H(H+1)/2 · W(W+1)/2：800·801/2 = 320,400；600·601/2 = 180,300；乘积 = 57,768,120,000 ≈ 5.8×10^10，不是 5.7×10^7 | 自行重算 |
| S15, S26 | `Regions of Interests` → `Regions of Interest` | 语法 | — |
| S20 | `2. Apply Selective Search on these feature maps and get object proposals` → `2. Apply Selective Search on the input image; project the proposals onto the feature maps` | Fast R-CNN 的 proposal 由 Selective Search 在输入图像上预先算好，再经 RoI 映射到 conv feature map；不是在 feature map 上做 Selective Search | arXiv:1504.08083 §2："takes as input an entire image and a set of object proposals"；RoI 是 conv feature map 上的矩形窗口 |
| S24 | `Gerschick` → `Girshick` | 作者姓名拼写 | arXiv:1504.08083 |
| S25 | Fast R-CNN 行：`Selective Search on feature maps` → `Selective Search on the input image`；`to generate predictions` → `to generate region proposals` | 同 S20（并保持红色高亮 run 不变） | arXiv:1504.08083 |
| S27 | `Non-Maximal Suppression` → `Non-Max Suppression` | 与 S8 标题术语一致 | — |
| S28 | `represent  one-hot vector` → `represent a one-hot vector` | 双空格 + 缺冠词 | — |
| S35 | `Two stage method (Faster R-CNN) get` → `Two-stage methods (Faster R-CNN) get` | 主谓一致/连字符 | — |
| S37 | `also label the pixels that belong to each thing` → `... each stuff category` | Panoptic = 实例分割（things）+ 给 stuff 打标签；原文"each thing"与实例分割重复，是错的 | 标准定义（Kirillov et al., CVPR 2019） |
| S45 备注 | `use 3 closest neighbors in x and y to construct cubic approximations` → `use 16 closest neighbors (4x4) in x and y ...` | 双三次插值使用 4×4 = 16 个邻点 | 自行验证：用 A=−0.75、边界复制重算，与 S45 图中 bicubic 数值 0.68/1.02/1.56/1.89… 完全吻合 |

## 已核实无误
- S8 NMS 例子：阈值 .7；.78>.7、.74>.7；蓝(.9)→橙(.8)被删，紫(.75)→黄(.7)被删；蓝-紫 0.05、蓝-黄 0.07 均 <.7，顺序一致。
- S9–S12：AP/mAP 定义；COCO mAP 取 IoU = .50:.05:.95 共 10 个阈值，1/10 求和正确；P/R 公式与"阈值↓ → precision↓ recall↑"方向正确。
- S14 的各项公式（W−w+1，(W−w+1)(H−h+1)，闭式求和）。
- S17–S19：224×224 前后一致；R-CNN 40–50 s ≈ 47 s（arXiv:1504.08083 Table 4）；Faster R-CNN 0.2 s ≈ 5 fps（arXiv:1506.01497 摘要）；~2000 proposals 一致。
- S28–S33 YOLO 张量：3×3×8；3×3×2×(5+3)=3×3×16；3×3×2×(5+4)=3×3×18；4×4×5×(5+5)=4×4×50；608/32=19，(19,19,5,85)，85=5+80。S30 的 (0.4,0.3)、(0.5,0.9) 与 y 向量图一致。
- S41 感受野 2L+1；两层 3×3（P=1）等效 5×5。
- S43 bed of nails / nearest；S44 max unpooling 位置；S45 bilinear 全部 16 个数值逐项重算正确；S46 转置卷积 2×2→3×3，输出 [[0,0,1],[0,4,6],[4,12,9]] 重算正确；S48 Mask head 28×28×C、box 4C。
- 页码连续，无隐藏页，无 TODO。

## 待你确认 / 未改
| 幻灯片 | 问题 | 建议 |
|---|---|---|
| S35 | "Two-stage (Faster R-CNN) 精度最好、One-stage (SSD) 快但不准"出自 2017 年的 speed/accuracy 图（Huang et al.），2026 年已过时：NMS-free/Transformer 一阶段检测器在精度和速度上都超过 Faster R-CNN | 保留为历史对比，但口头或加一句说明。可参考：YOLO26（NMS-free，arXiv:2601.12882）；RF-DETR（arXiv:2511.09554，nano 48.0 AP，2x-large 声称首个实时检测器 COCO >60 AP）。未改，因属教学取舍 |
| 全讲义 | 没有 YOLOv8–YOLO26、DETR/RT-DETR/RF-DETR、SAM/SAM 2/SAM 3 的内容（SAM 3 于 2025-11-19 发布，https://docs.ultralytics.com/models/sam-3 ） | 若需"update"，建议新增 1–2 页（本次不加页） |
| S10 | `??%` 已改成 `X%`；如果你是故意留空让学生口答，请恢复 | — |
| S25 | Fast R-CNN "2 s"：论文 Table 4 为 0.32 s（不含 proposal），≈2 s 是含 Selective Search 的量级 | 建议表头注明 "(incl. proposals)"；未改 |
| S25 | Faster R-CNN 行的 Limitations 单元格为空 | 可补，未改 |
| S6 vs S28 | Bbox 参数顺序 (x,y,w,h) vs (bx,by,bh,bw)（h 在 w 前） | 沿用 Andrew Ng 记号即可，但讲课时说明一下 |
| S29 vs S30 | S29 里有车的格子在左中，S30 "An Example Grid Cell" 高亮的是右中那辆车，但向量 (0.4,0.3,0.5,0.9) 画在同一例中 | 图为嵌入图片，未改；请核对示意是否一致 |
| S17 | 页面上有两个重叠的 slide-number 域（都显示 17） | 视觉上无影响，未改 |
| S7, S8, S9, S10, S14 | 这些文本框含数学公式，PowerPoint 存了一份"回退图片"（mc:Fallback）。PowerPoint 显示的是已改文字，但 LibreOffice/Keynote/Google Slides 仍会显示旧图（如 57 million、??%） | 用 PowerPoint 重新导出 PDF 即可 |
| S20, S21, S34 | LibreOffice 渲染下文字与图片轻微重叠（修改前就存在） | 请在 PowerPoint 里目测一下 |

## PDF 提示
同目录的 `L4 Object Detection and Segmentation.pdf` 是修改前导出的，现在比 pptx 旧，仍含 "57 million"、"??%"、"Gerschick" 等旧文字，需要重新导出。
