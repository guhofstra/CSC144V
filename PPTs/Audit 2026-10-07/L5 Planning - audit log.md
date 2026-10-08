# L5 Planning.pptx 审计日志(2026-10-07)

- 原件备份:`bak/audit-20261007/L5 Planning.pptx`(md5 9c9cbd3fdde825c72ec64e6cbda468c6)
- 修改后:22,114,250 字节,md5 31ad969afcefa67450b20d20af9863d7,70 页(与原件相同)
- 未发现 `~$` 锁文件(PowerPoint 未打开该文件)
- 编辑方式:直接改 slide/notes XML 中的文字 run 和 OMML 公式节点,其余部分字节级保持不变;validate.py(--original)通过。

## 摘要

| 类别 | 数量 |
|---|---|
| 已修改处(含备注) | 17 页 / 21 处 |
| 内容错误修正(含错别字/语法) | 20 处 |
| 事实更新(带来源) | 1 处(CARLA RSS 传感器) |
| 待你确认/未改 | 见下表 |

重要提示:含公式的文本框是 `mc:AlternateContent`,PowerPoint 读取 `Choice`(可编辑文字/OMML),`Fallback` 里是旧文字的位图。**我只能改 Choice,Fallback 图未动**(不允许改图)。PowerPoint 2010+ 显示 Choice,不受影响;LibreOffice/部分预览工具会显示旧位图。你在 PowerPoint 中保存一次会自动重生成 Fallback。受影响页:6、9、12、21、39、43、44、45、47、48、60、61、69 等含公式的框。

## 修改清单

| 页 | 修改前 → 修改后 | 原因 | 来源 |
|---|---|---|---|
| 6 | "Shortest path is S → C → **E** with length 10+12=22" → "S → C → **G**" | 终点是 G,图中没有 E;与第 11、13 页一致 | - |
| 7(备注) | "(Cannot finish here, must expand node B / since B's cost to S 5 is less than 22.)" → "...must expand node **C** / since **C's cost to S 10 is less than 25**.)" | 备注是旧版例子残留,与幻灯片正文"must expand node C, since total cost 25 > 10"矛盾 | - |
| 9 | "open[v] is sorted and popped in **decreasing** order of uCost+uvCost" → "**increasing**" | Dijkstra 用 MinHeap,每次弹出代价最小的节点(见伪代码 `MinHeap()`、第 10-11 页追踪) | - |
| 12(两处) | 同上,Dijkstra 与 A* 两段说明均 "decreasing" → "increasing" | 同上;A* 按 f=g+h 从小到大弹出 | - |
| 21 | "Rule1:" → "Rule 1:" | 与 "Rule 2:" 格式一致 | - |
| 33 | "binary encoding (upper left), or probabilistic encoding (upper right)" → "binary encoding (upper right), or probabilistic encoding (lower right)" | 按图片实际位置:二值栅格是右上图(Occupied-1/Free-0),概率栅格是右下图(0.94/0.12);左侧是原始航拍图,没有"upper left"的编码图 | 版面检查 |
| 37 | "such as as A*" → "such as A*" | 重复词 | - |
| 39 | "If a path exists, it will be found in finite time" → "If a path exists, the probability of finding it approaches 1 as running time increases" | 概率完备性(probabilistic completeness)的定义是成功概率随采样数/时间趋于 1,不是"有限时间内一定找到";原句与下一条"worst-case 时间可能很长"也不协调 | 标准定义(LaValle; Kavraki 1996) |
| 43 | "Fesnel integrals" → "Fresnel integrals" | 拼写 | - |
| 44 | "The optimization problem has closed-form solutions" → "has no closed-form solution; it is solved numerically" | 上一页(43)明说路径含 Fresnel 型积分、"has no closed-form equation",x(s_f),y(s_f) 约束需数值积分,优化问题不可能有闭式解;与 43 页自相矛盾 | Kelly & Nagy 2003 的数值参数优化做法;**如你本意不同请撤回** |
| 45 | 罚项 α(x_s(s_f)−x_f)+β(y_s(s_f)−y_f)+γ(θ_s(s_f)−θ_f) → 每个括号加平方 (…)² | 软约束罚项必须非负(平方或绝对值),线性项可取负值使目标无下界;与 Coursera 原课件一致 | - |
| 47 | "TTC can be computed by difference in speeds v_ego − v_lead divided by distance (arc length s)" → "…computed by distance (arc length s) divided by difference in speeds v_ego − v_lead" | TTC = s /(v_ego − v_lead),原文写反(量纲也不对:速度/距离=1/s)。**注意:同页右下角的 TTC 公式是图片,仍是 (v_ego−v_lead)/s,需要你替换图片**(见待确认) | - |
| 48 | v_k ≤ √(a_lat/κ_i) → v_**i** ≤ √(a_lat/κ_i) | 下标不一致,图中点为 κ1…κ5(i) | - |
| 59(备注) | "If the lateral distance **was becomes** non-safe" → "…becomes non-safe" | 语法 | - |
| 60 | "brake while steer to the right direction" → "brake while steering to the right direction" | 语法 | - |
| 61 | "brake, Since yellow…" → "since" | 大小写 | - |
| 69 | "a driving situations is safe" → "situation is";"requires to a counter measure" → "requires a counter measure" | 语法 | - |
| 69 | "The sensor evaluates longitudinal and lateral conflicts, but does not yet cover intersection conflicts." → "…and (in CARLA 0.9.16) also intersection conflicts." | 事实更新:CARLA 0.9.16 文档写明 `carla.RssSensor` 完整支持 ad-rss-lib v4.2.0 功能集,包括路口、stay-on-road 和行人等非结构化场景(仅 Linux 构建,需单独编译 RSS) | https://carla.readthedocs.io/en/0.9.16/adv_rss/ |

## 已核实无误

- 第 10-11 页 Dijkstra 追踪(A=2、C=10 → B=5 → G=25 → G=22,最短路 S→C→G=22)逐步重算正确。
- 第 13 页 A* 追踪:h(S)=11.5、h(C)=10.5、h(A)=22.5 均 ≤ 真实代价(22、12、23),估计总代价 20.5/24.5/22,弹出顺序 S→C→G 正确;同时满足一致性(consistency)。
- 第 7-8 页 BFS/DFS 例子(25 > 10 的判断)正确。
- 第 15 页练习:全部边权 ≥ 对应直线距离,h 可采纳;最短路 s→a→d→t = 5+2+1 = 8(与图中绿色路径一致)。
- 第 14 页:以最大限速除直线距离作为时间启发式——正确。
- 第 34-39 页 RRT/PRM 流程描述、第 40 页测验答案 B 正确。
- 第 43 页 θ(s) 积分、Simpson 公式(s/3n)[f0+4f1+2f2+…+fn];第 44 页弯曲能量定义;第 41 页 κ=1/R。
- 第 51-52 页:a=(v_f²−v_0²)/(2s)、v_fi=√(2a s_i+v_0²) 及梯形速度曲线三段公式推导正确。
- 第 64-67 页 RSS 安全纵向距离 d_min=[v_rρ+½α_maxρ²+(v_r+ρα_max)²/(2β_min)−v_f²/(2β_max)]_+ 与 Shalev-Shwartz 等 (arXiv:1708.06374) 一致;第 65 页推导、第 66 页"β_max 越大 d_min 越大"的论断正确。
- 第 3 页引用 Paden et al., IEEE T-IV 2016, 1(1):33-55,第 57 页 arXiv:1708.06374 引用核对无误。
- 链接可访问:Coursera "Motion Planning for Self-Driving Cars"(多伦多大学)、PathFinding.js、intel.github.io/ad-rss-lib。

## 待你确认 / 未改

| 页 | 问题 | 建议 |
|---|---|---|
| 47 | 右下角 TTC 公式是**图片**,仍为 (v_ego − v_lead)/s | 请替换为 TTC = s /(v_ego − v_lead)(要求 v_ego > v_lead);正文已改对,当前图文不一致 |
| 42 | "Con: curvature function and its derivatives may be discontinuous":五次多项式 x(u),y(u) 的曲率是连续的,真正的缺点是曲率无法直接约束/可能出现大峰值 | 建议改为 "curvature is not directly controlled and may exceed κ_max" 之类;涉及教学表述,未擅自改 |
| 12 / 13 | A* 说明用"admissible"即可保证最优,但伪代码带 closed set,严格需要 consistent heuristic(或允许重开节点) | 可加一句 "(consistent heuristic needed when using a closed set)";本页例子的 h 恰好满足一致性 |
| 5 | "BFS can finish after finding a path to the goal with total cost ≤ cost of all other partial paths" 对一般 BFS 并不成立(BFS 按边数而非代价展开);此为 Coursera 的叙述,用于引出 Dijkstra | 保留的话,可在备注里说明是"带代价排序的 BFS 变体" |
| 21 | 图注 "FSM-based example: traffic light changing color" 与插图(车辆的 Decelerate to Stop / Stop / Track Speed 状态机)不符 | 建议改为 "FSM-based example: vehicle behavior at a stop sign" |
| 24 | 状态机图片上 "Ego.Velocity >= 0"(Decelerate to Stop 的自环)与 "Ego.Velocity == 0" 的转移条件在 v=0 时重叠(图片内文字) | 图片,未改;可考虑把自环改为 ">0" |
| 28 / 21 | "Reinforcement Learning is a promising alternative":截至 2026 年业界(Tesla FSD 端到端、Waymo EMMA/多模态、UniAD/VAD 等)已在大量使用端到端/学习式规划,而非仅 RL | 属教学取舍,未改;可补一页"learning-based/end-to-end planning"概述 |
| 50 / 51 | 速度曲线图(线性斜坡、梯形)的 v 随弧长呈**直线**,而公式 v=√(2as+v₀²) 在 v–s 平面是曲线 | 图片,未改;可重绘或在图注说明为示意 |
| 59 | 正文 "A situation is dangerous if it is non-safe longitudinally"(纵向简化情形),备注写的是 "nonsafe both laterally and longitudinally"(RSS 原文的一般定义) | 建议正文加 "(in the same-lane case)" 或统一为一般定义 |
| 65 / 66 | 疑有重复的页码占位符(提取到两个 "65"、两个 "66") | 请在 PowerPoint 里检查是否有多余的页码文本框 |
| 3/18/29/53 | 大纲页备注是无关内容("Safety plan … The safety plan gives an overview…") | 建议清空备注 |
| 57 | 备注开头有残留 "Check on AI outputs open, transparent, technology neutral safety model…" | 建议清理 |
| 32 | 备注 "Assign speed value to every point on a given path. v …" 残留片段 | 可清理 |
| 66 | "These parameters should be determined by regulatory authorities…(NHTSA)"——可补充 **IEEE 2846-2022**(Assumptions in Safety-Related Models for ADS,2022-03-24 批准;2846a-2025 修订草案已批准)。该标准给出 RSS 类模型参数/假设的行业规范 | 来源 https://standards.ieee.org/ieee/2846/10831/ ;是否加入由你定 |
| 69 | "RSS is open-source … integrated into Baidu Apollo's planner module": Intel 已于 **2025-08-07 归档 ad-rss-lib 仓库、停止维护**(只读);Apollo 当前最新为 11.0,其 GitHub 首页未提及 RSS | 来源 https://github.com/intel/ad-rss-lib 、 https://github.com/ApolloAuto/apollo 。未改,因"曾集成"仍属实;建议加注 "(Intel archived ad-rss-lib in Aug 2025)",并自行确认 Apollo 11 是否仍含 RSS |
| 70 | "Usefulness: we give 100% guarantees to never cause accidents" 属 RSS 论文的条件性声明(依赖参数与假设),表述偏绝对 | 建议加 "under RSS assumptions" |
| 2 | 术语:本页 "Mission Planning",大纲/第 4 页为 "Route planning";"Local Planner" 与 "Motion Planning" 并用 | 建议统一或注明同义 |
| 17、36 等 | 外链(YouTube、PythonRobotics 等)无法逐一验证可用性 | 上课前点一遍 |

## 事实更新核查记录

- RSS / Apollo / CARLA:见上(CARLA 0.9.16 文档、ad-rss-lib 归档、Apollo 11.0)。
- 本课件不含 Waymo/Tesla/nuPlan/Autoware/ROS 2 等具体版本或统计数据,无需更新。
- 课件无统计数字类内容。

## 旧 PDF 提示

`L5 Planning.pdf`(2026-09-10 14:19)早于现在的 pptx,**需要从 PowerPoint 重新导出**,否则 PDF 仍含上述错误(如第 6 页 "S→C→E"、"decreasing order"、TTC 等)。
