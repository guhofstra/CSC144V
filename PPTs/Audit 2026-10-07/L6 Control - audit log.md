# L6 Control.pptx 审计日志(2026-10-07)

- 原件备份:`bak/audit-20261007/L6 Control.pptx`(md5 d60eb0893732d41be115df1a7bf88cc9)
- 修改后:14,316,230 字节,md5 69340112edf9bf1714f69b5b3ff33ee9,39 页(与原件相同)
- 未发现 `~$` 锁文件
- 编辑方式:仅改 slide XML 中的文字 run / 公式文字节点,其余字节级保持不变;validate.py(--original)通过。
- 注意:含公式的文本框是 `mc:AlternateContent`,我只能改 Choice(PowerPoint 读取),Fallback 位图未动;第 13、15、24、35、38、39 页在 LibreOffice 等预览里可能仍显示旧文字,PowerPoint 中保存一次即可重生成。

## 摘要

| 类别 | 数量 |
|---|---|
| 已修改 | 6 页 / 7 处 |
| 事实更新 | 0(本课件无版本/统计类事实;链接核查见下) |
| 待你确认/未改 | 见下表(其中第 12-13 页符号问题建议优先处理) |

## 修改清单

| 页 | 修改前 → 修改后 | 原因 | 来源 |
|---|---|---|---|
| 13 | λ₁,₂ 公式中 "…+4 v_r **k**_d" → "**K**_d" | 小写 k_d 与全文 K_d 不一致 | - |
| 15 | "Need to impose a maximum curvature radius to simulate a real car." → "Need to impose a **minimum turning radius (maximum curvature)** to simulate a real car." | 真实车辆受限的是最小转弯半径(即最大曲率);"最大曲率半径"术语错误 | - |
| 24 | "Which from the below statement about MPC are true?" → "Which of the statements below about MPC are true?" | 语法 | - |
| 35 | "average error, defined as sum of squared cte" → "…defined as **mean** of squared cte" | 代码 `return …, err / n`,返回的是平均值(且只累计后 n 步) | 第 35 页代码截图 |
| 38 | "Here are initialized to 0 for simplicity." → "Here the params (PID gains) are initialized to 0 for simplicity." | 句子缺主语(原公式对象丢失) | 与 38 页代码截图 `params = [0.0 …]` 一致 |
| 39 | "tuning PID controller by Gradient descent … step of adjustment dp[i] (the gradient) until convergence to minimum best_err" → "by coordinate descent (a gradient-free local search) … dp[i] (the step size, not a gradient) until convergence to a local minimum of best_err" | twiddle 不计算梯度,是逐坐标的局部搜索(hill-climbing);dp[i] 是步长不是梯度;且与第 38 页"twiddle() is a local optimization algorithm"一致 | 第 37 页算法框图及代码 |

## 已核实无误

- 第 5 页 PID 定义 e=r−y,u=K_p e+K_i∫e+K_d ė;第 7-10 页各增益影响及表格(K_p/K_i/K_d 对上升时间、超调、调节时间、稳态误差)符合常用教材表。
- 第 11-12 页横向控制模型:ḋ=v_r sinθ≈v_rθ、θ̇=u,线性化状态方程、P 控制 u=[K_d K_θ][d θ]ᵀ、闭环矩阵 [[0,v_r],[K_d,K_θ]] 均正确。
- 第 14 页:θ_th=π/6 rad 时 sin θ≈θ 误差约 5%;d_th=|K_θθ_th/K_d| 与饱和设计一致。
- 第 17-20 页 MPC:预测/控制时域(m,p)与图一致;线性 MPC 代价 xᵀQx+uᵀRu+终端项,x_{j+1}=Ax_j+Bu_j,u=−K x(LQR);非线性 MPC 约束形式正确。
- 第 22-23 页速度数字(PID:50→60→70→60→50 km/h;MPC:50→40→30→20→15 km/h)与"加速到 70 km/h"文字一致,单位均为 km/h。
- 第 26 页运动学/动力学公式;第 28 页自行车模型:tanδ=L/R、θ̇=v tanδ/L、ẋ=v cosθ、ẏ=v sinθ(对 δ 非线性、对 v 线性);R 为后轮到 ICR 距离。
- 第 29-31 页:圆周运动更新 x_c=x−R sinθ、y_c=y+R cosθ、新位姿 x=c_x+R sinθ'、y=c_y−R cosθ';直线近似推导及四个特殊方向(0、π、π/2、3π/2)正确;代码与公式逐行对应。
- 第 36-37 页:dt≠1 时 diff_cte=(cte−prev_cte)/dt、int_cte+=cte·dt;twiddle 的 +dp、−2dp、×1.1、×0.9 步骤与代码一致。
- 第 38 页 dparams[1]=dparams[2]=0 ⇒ P 控制,与 35 页 params[0..2]=K_p,K_d,K_i 对应一致。
- 第 39 页线性化 [v, vθ, u]ᵀ 正确。
- 链接核查:Tübingen "Self-Driving Cars"(Winter 25/26)可访问;Medium MPC 文章会 302 重定向到 david010.medium.com(仍可用)。

## 待你确认 / 未改

| 页 | 问题 | 建议 |
|---|---|---|
| **12-13(重要)** | 第 12 页误差动力学写作 [ė_d ė_θ]ᵀ = −[ḋ θ̇]ᵀ = [[0,−v_r],[−K_d,−K_θ]]·**[d θ]ᵀ**(右边是状态 x,不是误差 e)。第 13 页却把该矩阵 [[0,−v_r],[−K_d,−K_θ]] 当作闭环极点矩阵,得 λ²+K_θλ−v_rK_d=0、λ=−K_θ/2±…。但真实闭环 ẋ=[[0,v_r],[K_d,K_θ]]x 的特征方程是 **λ²−K_θλ−v_rK_d=0**,λ=**+**K_θ/2±½√(K_θ²+4v_rK_d)。结果:按第 13 页选 K_θ>0 以为稳定,实际闭环是不稳定的;稳定要求 **K_θ<0 且 K_d<0**(与"d>0 向左偏则向右转"的直觉一致)。临界阻尼条件 K_d=−K_θ²/(4v_r) 不受影响 | 方案 A:第 13 页矩阵改为 [[0,v_r],[K_d,K_θ]]、多项式改 λ²−K_θλ−v_rK_d、根改 K_θ/2±…,并注明 K_θ<0;方案 B:第 12 页把误差动力学改写为 ė=[[0,v_r],[K_d,K_θ]]e(因 e=−x,矩阵与闭环矩阵相同),第 13 页同样用该矩阵,结论同方案 A。涉及多处公式和教学推导,未擅自改 |
| 17 | "Set initial state to predicted state x[k]"——MPC 每步的初始状态应是**测量/估计**得到的当前状态(某些教材用观测器预测值)。另 "while in the time interval [k−1,k]" 含义不明 | 建议改为 "Set initial state to the current (measured/estimated) state x[k]" |
| 32 vs 34 | 第 32 页 "Lesson 15: PID Control",第 34 页 "Lesson 16: Problem Set 5, 4. Quiz" ——课号是否一致(Udacity CS373 的 Unit 5 Control 与 Lesson 编号)无法核实 | 请对照 Udacity 原课程核对 |
| 32、38 | `classroom.udacity.com/courses/cs373` 链接:Udacity 旧 classroom 域名已多年重组,WebFetch 被 robots 拒绝,**无法验证是否可用** | 上课前点开确认;或改为 CS373 课程新页面/Georgia Tech CS7638 |
| 35、37 | 代码截图中保留 Udacity 模板的 "# TODO: your code here / Add code here" 注释 | 是教学截图,仅提示 |
| 35(备注) | 备注 "(Minus signs can be removed without affecting correctness.)" 不严谨:去掉负号相当于 K 取负值,"K_p should be positive" 的检查随之变化 | 建议改为 "(sign convention: absorbed into K if minus signs are removed, then K_p<0)" 或删除 |
| 20 | 非线性 MPC 目标 Σ_{j=t}^{t+T} C(x_j,u_j) 求和到 t+T,而控制只到 t+T−1(u_{t+T} 未定义);"x_j … minimized with term x_{t+T}ᵀQ_f x_{t+T}" 一句指代略乱 | 小问题,建议求和上限改 t+T−1 加终端项 |
| 10 | 表格第一列为小图片(缺少可编辑文字的 K_p/K_i/K_d 行标签) | 图片,未改 |
| 6 | 上升时间定义为"到达稳态值的 1.0−δ"(与图一致),教材常用 10%-90%;属约定差异 | 可在备注注明 |
| 3/21 | "The most common control algorithms in automotive systems are PID and MPC"——量产车辆中 PID 与 MPC 仍占主流;另 Apollo/Autoware 的横向控制多为 LQR/MPC,Tesla 等端到端系统的控制模块情况未公开,不宜断言 | 属教学取舍;本课件无需更新,未改 |

## 事实更新核查记录

本课件不含具体的 Apollo/Autoware/ROS 2 版本号、法规或统计数字,也没有纯追踪(pure pursuit)、Stanley、LQR 的专门页面(LQR 只在第 20 页以 u=−Kx 带过),因此没有"过时事实"需要更新。

## 旧 PDF 提示

`L6 Control.pdf`(2026-09-10 14:24)早于现在的 pptx,**需要从 PowerPoint 重新导出**(PDF 仍含 "maximum curvature radius"、"Gradient descent" 等旧文字)。

---

# 第二轮修改（2026-10-07，应你的要求）

- 本轮修改前备份：`bak/audit-20261007/L6 Control (pre-LQR-edit).pptx`
- 修改后：14,404,794 字节，md5 e1090fc7c0094ea76cb0b7fffb9881e2，**50 页**（原 39 页 + 新增 11 页），validate.py（--original）通过；设备上核对 md5 与页数一致。

## 1. 采用方案 A 修正极点公式（原第 12–13 页，现仍为第 12–13 页）

| 页 | 修改 |
|---|---|
| 13 | 矩阵 [[0,−v_r],[−K_d,−K_θ]] → **[[0,v_r],[K_d,K_θ]]**；特征多项式 λ²+K_θλ−v_rK_d → **λ²−K_θλ−v_rK_d**；根 λ=−K_θ/2±… → **λ=K_θ/2±½√(K_θ²+4v_rK_d)**；新增一条 "Stable closed loop requires K_θ<0 and K_d<0"。临界阻尼条件 K_d=−K_θ²/(4v_r) 不变（已数值验证重根为 K_θ/2）。 |

## 2. 采用的其它建议

| 页（新页码） | 修改 |
|---|---|
| 17 → 现第 21 页 | "Set initial state to predicted state x[k]" → "Set initial state to the **current (measured/estimated) state** x[k]" |
| 20 → 现第 24 页 | 非线性 MPC 目标：求和上限 t+T → **t+T−1**，并补终端项 **+C_f(x_{t+T})** |
| 35 → 现第 46 页（备注） | 备注改为 "(Sign convention: if the minus signs are removed, they are absorbed into the gains, i.e., K_p < 0.)" |
| 6（备注） | 备注补充：本页上升时间定义为到达稳态值的 1−δ，教材常用 10%–90% |
| 未改（仍需你自行核对，原页码） | 第 32/34 页 Udacity 课号与旧 classroom 链接（无法验证）；第 35/37 页截图里的 Udacity TODO 注释；第 10 页图片行标签 |

## 3. 新增 11 页

Outline 全部更新为 6 项：PID Control / LQR / MPC / Kinematic bicycle model / Geometric path tracking: Pure Pursuit & Stanley / Twiddle()。

| 新页码 | 标题 | 内容 |
|---|---|---|
| 16 | Outline（LQR 高亮） | 新增 |
| 17 | LQR: Linear Quadratic Regulator | 离散/连续时间 LQR、DARE/CARE、K 离线计算、框图 |
| 18 | LQR Example: Lateral Control | 用第 11–12 页横向模型推出闭式增益 K_d=−√(q_d/r)、K_θ=−√(q_θ/r+2v_r√(q_d/r))，与第 13 页多项式对应；示例 v_r=10 m/s、q_d=q_θ=r=1：K_θ=−√21≈−4.58，极点 −2.29±2.18j；响应图 |
| 19 | LQR: Tuning and Trade-offs | Bryson 规则、与极点配置/MPC 的关系、速度调度与曲率前馈、Apollo 的 LQR 横向控制器；Q/R 效果表与设计步骤 |
| 36 | Outline（Geometric path tracking 高亮） | 新增 |
| 37 | Pure Pursuit: Geometry | 推导 R=L_d/(2 sinα)、κ=2 sinα/L_d、δ=arctan(2L sinα/L_d)；示例 L=2.5、L_d=5、α=20° → κ=0.137、δ=18.9° |
| 38 | Pure Pursuit: Lookahead Distance | κ=2y_g/L_d²、L_d=k_v v+L_0、截弯误差≈L_d²/(8R)、算法步骤；仿真：L_d=2/5/10 m → 峰值误差 0.02/0.13/0.55 m |
| 39 | Stanley Controller | δ=ψ+arctan(ke/v)、符号约定、软化常数 k_s；示例 → δ≈11.4° |
| 40 | Stanley: Why It Converges | ė=−ke/√(1+(ke/v)²)，小误差指数收敛、时间常数 1/k；收敛曲线 |
| 41 | Pure Pursuit vs. Stanley vs. LQR | 运动学自行车模型仿真（v=6 m/s、起点偏 1.5 m、R=20 m 弯道）：弯道内峰值误差 PP 0.11 m / Stanley 0.02 m / LQR 0.01 m（无前馈 0.30 m） |
| 42 | Choosing a Lateral Controller | PID / Pure Pursuit / Stanley / LQR / MPC 对比表 |

- 所有新页含讲稿备注（推导与数值检查）。公式为原生 PowerPoint 公式（OMML），与本 deck 其它页一致；LibreOffice 等预览会显示纯文本近似，在 PowerPoint 里显示为正常公式。
- 已验证：LQR 闭式增益与 scipy CARE 数值解在随机参数下一致；所有示例数字重新计算；仿真数据来自脚本（运动学自行车模型 L=2.5 m）。
- 事实来源：Apollo 文档 "How to Tune Control Parameters"（LQR 横向控制器，4 个状态）；Autoware 控制文档（lateral_controller_mode 默认 mpc，可选 pure_pursuit）；Hoffmann et al., ACC 2007（Stanley 控制律）；Coulter, CMU-RI-TR-92-01, 1992（Pure Pursuit）。
- 注意：第 13、24 页含 AlternateContent 公式，回退预览图仍是旧文字；请在 PowerPoint 里保存一次。旧 `L6 Control.pdf` 需要重新导出。
