# L5 LiDAR Perception.pptx - 审计日志 (2026-10-07)

- 原件备份: `PPTs/bak/audit-20261007/L5 LiDAR Perception.pptx`(未动)
- 编辑后: 50 页 (与原件相同), 大小 4,274,654 bytes, md5 `b2e45b76b137ccb4a7ce643e46a527ed`, validate.py 通过, LibreOffice 可正常打开并渲染 50 页
- 检查到 `~$` 锁文件: 无 (PowerPoint 未打开该文件)
- 方法: 直接改 slide/notes XML 中的单个 `<a:t>` 文本 run, 其余 zip 条目逐字节保持不变 (只有 slide7 / slide13 notes / slide50 / notesSlide7 共 4 个部件有改动)

## 1. 汇总

| 项目 | 数量 |
|---|---|
| 实际修改 | 4 处 (幻灯片正文 2 处, 备注 2 处) |
| 事实更新 (带来源) | 1 处 (Luminar 破产) + 1 处备注补充 |
| 计算/公式复核 | 全部通过, 未发现数值错误 |
| 待你确认 / 未改 | 12 项 (见第 4 节) |

## 2. 修改清单

| # | 幻灯片 | 之前 → 之后 | 原因 | 来源 |
|---|---|---|---|---|
| 1 | 7 (表格 "Examples" 行, Pulsed ToF 列) | `Hesai, Ouster, Luminar, Waymo` → `Hesai, Ouster, Waymo, Luminar (Ch. 11, 2025)` | 公司状态过时: Luminar 于 2025-12-15 申请 Chapter 11, 激光雷达业务经 2026-01-27 法院批准以 3300 万美元出售给 MicroVision, 半导体子公司以 1.1 亿美元卖给 Quantum Computing Inc. 保留 Luminar 作为 pulsed-ToF 例子 (产品技术仍然正确), 只标注公司状态, 未替换你的例子选择 | https://www.therobotreport.com/lidar-maker-luminar-declares-bankruptcy-quantum-computing-buy-subsidiary/ ; https://chapter11cases.com/blogs/news/luminar-technologies-proposes-liquidation-through-143-million-asset-sale-to-quantum-computing-and-microvision ; https://techcrunch.com/2026/01/27/luminar-receives-a-larger-33-million-bid-for-its-lidar-business/ |
| 2 | 7 备注 | `Most deployed automotive LiDAR is pulsed ToF.` → `Most deployed automotive LiDAR is pulsed ToF (Luminar filed for Chapter 11 in Dec 2025; its lidar assets were sold to MicroVision in Jan 2026).` | 与 #1 对应, 讲课时的口头说明 | 同上 |
| 3 | 13 备注 | `only 1.8% of the signal survives at 100 m` → `only about 2% of the signal survives at 100 m (1.8% for the rounded alpha = 0.02 /m plotted)` | 重算: alpha = 3.91/200 = 0.01955 /m, exp(-2*0.01955*100) = exp(-3.91) = 2.0%; 1.8% 只对应图中取整的 alpha = 0.02 (exp(-4) = 1.83%). 图 (原生图表) 本身正确, 只是备注没说明取整 | 自行计算 |
| 4 | 50 (参考文献 [18]) | `Adversarial sensor attack on LiDAR-based perception, ACM CCS 2019` → `Adversarial sensor attack on LiDAR-based perception in autonomous driving, ACM CCS 2019` | 论文标题被截断; 正式标题为 "Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving" | Cao et al., CCS 2019 |

## 3. 已核实无误 (简表)

**公式/数值 (逐项重算):**
- 幻灯片 5: R = c·Δt/2; 1 ns -> 15 cm; 5 cm 精度需 0.33 ns; 200 m -> 1.33 µs; 脉冲率上限 c/2R_max = 750 kHz 全部正确
- 6: 球坐标 -> 笛卡尔公式及反变换正确; 0.1° @ 100 m = 0.1745 m (≈ 0.17) 正确
- 9: 0.2° 点间距 0.17 / 0.35 / 0.70 m (50/100/200 m) 正确; 0.5 m 行人阈值 0.5/0.003491 = 143 m 正确; 图表数据 (chart1) 与公式一致
- 11: 20 m -> 0.13 µs, 200 m -> 1.3 µs 正确; 表中 20 m/200 m, 0.5°/0.05°, 10/1000 SPAD, 0.13/1.3 µs 与 Waymo ISSW 2024 原 PDF 一致
- 13: Beer-Lambert exp(-2αR), Koschmieder α ≈ 3.91/V; chart2 四条曲线数值正确 (dense fog 100 m 处 1.83%)
- 15: 128 × 1800 × 10 = 2.304 M 点/s; ×16 B = 36.9 MB/s; ×3600 = 133 GB/h 正确
- 18: tan(0.5°)·100 m = 0.87 m (≈ 0.9) 正确; 19: 20 m/s × 0.1 s = 2 m, 72 km/h = 20 m/s 正确
- 21: 800 × 800 × 40 = 25.6 M; 0.19 M/25.6 M = 0.74% < 1% 正确
- 25: 11,889 -> 1,613 = -86.4%; 26: N = ln(0.01)/ln(1-0.5³) = 34.5 -> 35 正确
- 28: RANSAC 迭代次数表 10 个数 (3,4,7,11,17,35,49,169,459,4603) 全部重算一致
- 31: 0.2° 间距 0.07 m @ 20 m, 0.21 m @ 60 m; 0.5° 垂直间距 0.17 / 0.52 m 正确
- 41: PointPillars (P,N,D) = (12000,100,9), D = 4 + 3 + 2 = 9, 62 Hz 与论文一致; 39: PointNet 结构 (64,64)/(64,128,1024)/(512,256,k) 正确
- 44: KITTI IoU 0.7/0.5, nuScenes 中心距离 0.5/1/2/4 m, Waymo APH + L1/L2 正确
- 47: 100 ms × 60 m/s = 6 m; chart3 (15/30/60 m/s × 50...300 ms) 全部正确
- 幻灯片编号交叉引用: "slide 9", "slide 14", "slide 21", 备注中 "slides 4-22 / 23-48" 全部指向正确页; 无 `??`/TODO/占位符
- 数据集 (22): KITTI 7,481/7,518, HDL-64E 10 Hz; nuScenes 1,000 scenes × 20 s, 1.4 M boxes, 23 classes, 32-beam 20 Hz; Waymo Open 1,150 scenes, 5 LiDAR (1 mid + 4 short); SemanticKITTI 均正确
- Waymo ISSW 2024 原 PDF (https://imagesensors.org/Past%20Workshops/2024%20ISSW/Presentations/R05-1.pdf) 核对: 60° scan / 25% duty vs 360° / 100%; SPAD PDE 5% -> 40% @ 915 nm; O(10) sensors, 100s of millions readings/s; 反射率 < 5% 与 10-30+ dB; 夜间 > 200 m 检测 -- 与幻灯片一致
- 文献年份/会议 (CenterPoint CVPR 2021, BEVFusion ICRA 2023, PointPainting CVPR 2020, SWFormer ECCV 2022, PV-RCNN CVPR 2020, LaserNet CVPR 2019, RangeNet++ IROS 2019 等) 无误

## 4. 待你确认 / 未改

| 幻灯片 | 问题 | 建议 |
|---|---|---|
| 3, 47 备注 | "links forward to adversarial attacks" / "Link to the adversarial attacks lecture": 按编号, 对抗攻击讲座 L4.1-L4.3 在 L5 之前 | 若 L5 实际排在 L4.x 之后, 改成 "links back to" / "builds on the adversarial attacks lectures" |
| 文件名/编号 | 目录里有两个 "L5": `L5 LiDAR Perception` 与 `L5 Planning` | 其中一个重新编号 (例如 L5 -> L5.1/L5.2 或 Planning -> L6, Control -> L7), 并同步课程网站 |
| 11, 46 | "Waymo's vehicle combines four short-range perimeter LiDARs, one long-range 360° LiDAR" / "4 short-range + long-range 360° LiDAR": 这是 ISSW 2024 讲座 (第 5 代) 的配置. Waymo 第 6 代 Driver (2024-08 发布, 2026-02 起无安全员运营) 为 13 摄像头 + 4 激光雷达 + 6 雷达; 第 5 代为 29 摄像头 + 5 激光雷达 | 保留 (已注明出处 ISSW 2024); 若想讲当前状态, 加一句 "6th-gen: 4 lidars total"; 第 6 代 4 个雷达中长/短程的划分我没找到可靠来源, 故未改. 来源: https://waymo.com/blog/2024/08/meet-the-6th-generation-waymo-driver/ ; https://electrek.co/2026/02/12/waymo-begins-fully-autonomous-ops-with-6th-gen-driver-targets-1m-weekly-rides/ |
| 1 备注 | "Two-lecture module (about 150 minutes)" 而幻灯片 2 的分段时间合计 35+30+35+40 = 140 min (实验 ~45 min 在 48 页备注另算) | 教学安排问题, 未改; 如要一致可改为 "about 140 minutes" |
| 49 | "Always evaluate with IoU-based AP": 但 44 页说 nuScenes 用中心距离而非 IoU | 可改为 "Always evaluate with AP (IoU- or distance-based matching)" |
| 49 | 脚注 "Links are listed on the next slide." 但 50 页的 Tübingen / Utah 条目没有 URL | 补 URL 或改脚注为 "References on the next slide" |
| 44 | 例子 "0.9 m shift and 10° heading error -> BEV IoU = 0.45": 我用 4.4 × 1.9 m 框重算, 结果依平移方向在 0.35 (沿宽度方向) 到 0.58 (沿长度方向) 之间, 0.45 对应斜向平移, 与图一致 | 无需改; 可在备注写明平移方向 |
| 32 | "15.2 m² vs. 8.7 m²": 依赖图中点云 (只含可见面), 无法独立重算; 8.7 m² 与 4.4 × 1.9 = 8.36 m² 量级一致 | 未改 |
| 17 | 4,100 点 @ 7 m vs 740 点 @ 24 m (比值 5.5) 与 1/R² 预期 (24/7)² = 11.8 不同; 38 页写 "Density falls ≈ 1/R²" | 合成场景中两辆车朝向/遮挡不同所致; 可在备注加一句说明, 避免学生追问 |
| 22 | Waymo Open "1,150 scenes × 20 s" 是 v1.0 感知集; 数据集后续版本有扩充 | 属教学简化, 未改 |
| 7 | 其他厂商只写了名字 (Hesai, Ouster, Aeva, Aurora): 本次未发现需要改动的过时事实 (Hesai 2026 年仍在扩产, 见 https://techcrunch.com/2026/01/05/chinas-hesai-will-double-production-as-lidar-sensor-industry-shakes-out/ ) | 如要加 "Luminar 资产归 MicroVision" 等, 由你决定 |
| 备注 (多页) | 备注中英式拼写 (neighbour, minimises) 与幻灯片美式拼写 (neighbor) 混用 | 风格问题, 未改 |

## 5. PDF 过期提醒

`L5 LiDAR Perception.pdf` (修改于 2026-10-07 13:10) 早于现在的 pptx (2026-10-07 22:39), 需要从 PowerPoint 重新导出 PDF. 7 页表格 "Examples" 行因多了文字会折成两行, 导出后请目测该页.
