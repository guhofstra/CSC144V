# CSC144V / PPTs — 全部 pptx Content & Update Audit 总报告（2026-10-07）

范围：顶层 14 个 pptx（不含 DRL by Kalle / Lab2.bak / Lab3 / OLD 子文件夹，以及只有 PDF 的 L7.x、L8）。
原文件已备份到 `PPTs/bak/audit-20261007/`。每个 deck 的详细记录（before → after、来源 URL、待确认项）在本文件夹的 `<deck> - audit log.md`。
所有 deck 均已原地修改、设备上核对 md5 与页数（与备份逐一一致），没有 `~$` 锁文件。检查在 LibreOffice 渲染下完成，没有在 PowerPoint 里打开过。

## 一、各 deck 概况

| Deck | 页数 | 改动 | 最重要的发现 |
|---|---|---|---|
| L0 course overview | 5 | 4 | "Three lab assignments"→Two（与网站、成绩比例一致）；上课时间/教室与课程网站不符（未改）；office hours 8:00–9:40 PM 疑为 AM |
| L1.1 Introduction Overview | 29 | 14 | 死亡/受伤数据更新到 NSC 2024（42,789 / 4.9M）；"at most L2" 与 Waymo 现状及 Mercedes L3 图矛盾；Cruise 状态（GM 2024-12 终止）；nuTonomy→Motional |
| L1.2 AV Sensors V2X HD Maps | 35 | 15 | IMU 全称 Unit、角速度；DSRC 全称；C-V2X 已胜出（FCC 2024-11）；S29 "2x"→~1.8x |
| L1.3 HWSW Platforms Ethics | 36 | 14 | Thor 2000 TOPS→1000 INT8 TOPS（图片仍写 2000）；DRIVE 软件非开源；Autoware.AI 已 EOL；S33 two/five 与 3 对 3 场景矛盾 |
| L2 Intro to ML | 30 | 10 | S20 混淆矩阵行标签 Pos/Neg 弄反；S19 AUC 公式；S24 AdaGrad/RMSProp 不是动量法；数学全部重算无误 |
| L2.1 Intro-to-Neural-Networks | 118 | 13+5 | Adam = Adaptive *Moment* Estimation；ImageNet 1.4M→1.2M；D 次多项式拟合 D+1 点；87 页备注 `[Slide N]` 编号从 S30 起错位 2，已改 |
| L3 Convolutional Neural Networks | 68 | 7 | LeNet-5 年份 1989→1998；VGG-16 参数 60M→138M；same padding 例子；引用页码 |
| L4 Object Detection and Segmentation | 49 | 19 | S14 滑窗总数 57M→约 58B；Panoptic stuff/thing；Fast R-CNN 的 Selective Search 作用于输入图像；bicubic 4×4=16 邻点 |
| L4.1 Adversarial Attacks | 34 | 7 | 标题页 "L3.2"→"L4.1"、出处 NeurIPS 2018；S8 salt-and-pepper 的 ℓ2/ℓ∞ 说反了；S21 求和下标 |
| L4.2 Adversarial Attacks for AD | 43 | 15 | 交叉引用旧编号；S27 "3+3≠8" 表述；S33 "<0.9 s"；13 个引用数字对照论文摘要全部一致 |
| L4.3 Latency and Availability Attacks for AD | 50 | 10 | 交叉引用旧编号；备注算术 103.5 ms；算术链全部重算无误 |
| L5 LiDAR Perception | 50 | 4 | 全部计算无误；Luminar 2025-12 申请 Chapter 11（LiDAR 业务 2026-01 卖给 MicroVision）已标注；参考文献 [18] 补全 |
| L5 Planning | 70 | 21 | S6 最短路终点 G；S9/S12 decreasing→increasing；S47 TTC 公式文字已改但同页图片公式仍是旧的；S44 "no closed-form" |
| L6 Control | 39 | 7 | S39 twiddle 不是 gradient descent；S15 minimum turning radius；S35 mean；**S12–13 极点矩阵符号有误（未改）** |

## 二、需要你拍板的事项（agent 没有擅自决定）

1. **L6 Control S12–13（最重要）**：真实闭环特征方程是 λ² − K_θλ − v_r·K_d = 0，稳定需要 K_θ < 0 且 K_d < 0；按现在的写法选 K_θ > 0 会不稳定。涉及多处公式，日志里给了两种修法。
2. **L0**：上课时间/教室（slide: MW 11:20–12:45, SIC 200；网站: MW 9:40–11:05, SIC 231）、office hours PM/AM、"Course tutor: TBD"、标题里的 "/291R"、文件元数据仍是旧 Java 课。
3. **图片里的错误（agent 无法改图，需要你重做或替换）**：L1.3 S8 Thor 图（2000 TOPS）、S12 Mobileye 图 TOPS；L2 S14 / L2.1 S33 图里 −log(.353)=0.452 是以 10 为底，与文字的自然对数（1.041）不一致；L2.1 S32 预测分布加起来 107%、S29 交叉熵缺负号；L3 S46 一格 −3 应为 −2 且 softmax 底数不一致；L4.1 S16 "PDG" 笔误及 74.3% vs S33 的 74.4%；L5 Planning S47 右下角 TTC 公式图片。
4. **课程编号**：现在 L3.2/3.3/3.4 已是 L4.1/4.2/4.3（已改交叉引用）；L5 有两个（LiDAR Perception 与 Planning）；L4.2 S13/S14、L4.3 S12 备注 "Recall L1.3 … LiDAR" 现在指向错的讲（L1.3 是 HW/SW 与伦理）；L5 LiDAR S3/S47 "links forward to adversarial attacks" 与新顺序相反。
5. **事实更新是否继续**：L1.1 S15 Tesla 获胜一页（2025 Benavides 案 Tesla 担责 33%、赔偿 $243M，2026-02 维持原判）；L1.1 S16–18 2022 年加州数据；L1.2 S6 传感器表是 2018 年快照（Cruise 已停、Waymo 第 6 代配置）；L1.3 S36 美国 AV 立法（2026-02 提出 SELF DRIVE Act）；L2.1 S94 Tesla 2021 年架构（FSD v12 起端到端）、S83 可补 AdamW/Muon；L4 S35 Faster R-CNN vs SSD 论断及全讲没有 YOLOv8+/DETR/SAM 3；L5 Planning S66/S69 可补 IEEE 2846-2022 与 ad-rss-lib 归档。
6. **L4.3 S50 参考文献**缺正文引用的多篇；S29 "CCS 2026" 未能在 arXiv 页确认（你自己的研究内容，未改）。
7. **L1.1 S10** 的图片仍是 nuTonomy 旧图；**L2 S9** 图中 "Ouput" 拼写错；**L3 S26** 标题 "???"（可能是故意的提问，未改）。
8. 备注里的无关残留建议清空：L5 Planning S3/18/29/53/57，L3 S39（"Safety plan"），L1.1 S29（已重复两遍）。

## 三、共性问题

- **PDF 已落后于 pptx**：同目录所有对应的 `.pdf` 都是旧版，需要从 PowerPoint 重新导出。
- **公式框是 mc:AlternateContent**（L2 S19、L2.1、L3 S18/28/55、L4 S7–10/14、L4.1 S8/21、L5 Planning 等）：修改写入了 Choice 部分；LibreOffice/Keynote/Google Slides 看到的仍是旧 Fallback 位图。请在 PowerPoint 里打开并保存一次，预览才会刷新。
- 没有联网核实外部链接（课程网站、Udacity、classroom 等），也没改任何 PDF、bak、DRL by Kalle、Lab2.bak、Lab3、OLD 里的文件。
- 学校排课、考试日期等只能由你核对。
