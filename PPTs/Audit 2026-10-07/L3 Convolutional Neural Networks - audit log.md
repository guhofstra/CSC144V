# L3 Convolutional Neural Networks.pptx - 审计日志 (2026-10-07)

备份原件: `PPTs/bak/audit-20261007/L3 Convolutional Neural Networks.pptx`（md5 df9fbea0e89308f9f2849d5f975316ed）
修改后: 68 张幻灯片（数量不变），md5 7a6f45fa0b76ff77ed02fb9b78cc1588，文件大小 13,958,792 字节。
未发现 `~$` 锁文件。
修改方式: 直接在原 slideN.xml 中替换文字 run，其余所有部件与原件逐字节一致；validate.py 通过。

## 汇总

| 类别 | 数量 |
|---|---|
| 修改处数 | 7 处（第 18, 28, 48, 50, 51, 52, 55 张各 1 处） |
| 其中事实更正（联网核实） | 3 处（第 50, 52, 55 张） |
| 其中计算/公式/交叉引用错误 | 2 处（第 28, 51 张） |
| 其中拼写 | 2 处（第 18, 48 张） |
| 待你确认/未改 | 12 项 |

## 全部改动

| 幻灯片 | 修改前 → 修改后 | 原因 | 来源 |
|---|---|---|---|
| 18 | `Pytorch code for a CONV layer` → `PyTorch code for a CONV layer` | 官方写法 PyTorch（与第 17 页标题一致） | - |
| 28 | `e.g., F<3 ⇒ P=0` → `e.g., F=1 ⇒ P=0` | Same padding 公式 P=(F−1)/2：F=1 时 P=0，与同页 "Common settings: F = 1, S = 1, P = 0" 一致；F<3 会包含 F=2，此时 P=0.5，不是整数，错误 | - |
| 48 | `prune to overfitting` → `prone to overfitting` | 拼写 | - |
| 50 | 标题 `LeNet-5 (LeCun et al. 1989)` → `LeNet-5 (LeCun et al. 1998)` | LeNet-5 出自 LeCun, Bottou, Bengio, Haffner, "Gradient-based learning applied to document recognition", Proc. IEEE, Nov 1998；1989 年是更早的 LeNet-1 / 反向传播邮编识别工作 | http://yann.lecun.com/exdb/lenet/ （参考文献 [LeCun et al., 1998]） |
| 51 | `p. 46 “Summary of 3 Types of CNN Layers”` → `p. 47 “Summary of 3 Types of CNN Layers”` | 该标题的幻灯片是第 47 页（第 46 页是 "A Complete CNN Example"）；p. 28、p. 41 的引用是对的 | - |
| 52 | `1,000 object classes, 1.4 M labeled images` → `1,000 object classes, 1.2 M labeled training images` | ILSVRC-2012：训练 1,281,167，验证 50,000，测试 100,000（测试集无公开标签）；1.4M 把无标签测试集也算上了。与 L2.1 第 88 页同步更正 | https://www.tensorflow.org/datasets/catalog/imagenet2012 |
| 55 | `Total # params: 60M` → `Total # params: 138M` | 60M 是 AlexNet（第 53 页）的参数量；VGG-16（配置 D）为 138M | https://arxiv.org/pdf/1409.1556 （Table 2） |

重要提示（渲染缓存）: 第 18、28、55 页含 PowerPoint 公式对象（mc:AlternateContent），其 Fallback 是一张旧版"整页图片"。PowerPoint 会读取公式版本（已更新），但 LibreOffice / Keynote / Google Slides 等会显示 Fallback 旧图（仍是 Pytorch / F<3 / 60M）。在 PowerPoint 中打开并保存一次即可重新生成 Fallback；导出 PDF 请用 PowerPoint 导出。

## 已核实无误

- 第 6–7 页：垂直边缘检测示例（Prewitt 型 30/−30，Sobel 型 40/−40）逐格复算无误。
- 第 12–16 页：32×32×3 输入、5×5×3 滤波器 → 28×28；75 次乘法；6 个滤波器 → 28×28×6；6×6×3 输入、3×3×3 滤波器 → 4×4×1 / 4×4×2。
- 第 17–18 页：Conv2d(in_channels=2, out_channels=1/3, kernel_size=3) 描述一致。
- 第 19 页：308 + (−498) + 164 + 1 = −25。
- 第 24–27 页：7×7 / 3×3：stride 1 → 5×5；stride 2 → 3×3；stride 3 加 P=1 → 3×3（⌊(7+2−3)/3⌋+1 = 3）。
- 第 28–31 页：same padding 公式推导；5×5 → 3×3、5×5、stride 2 时 3×3，均复算正确。
- 第 32 页：28×28×10 与 32×32×10；每个滤波器 5·5·3+1=76，共 760 参数。
- 第 34 页：1×1 卷积 56×56×64 → 56×56×32；65 × 32 = 2080。
- 第 42 页：最大池化 [6 8; 3 4]，平均池化 [3.25→3.3, 5.25→5.3; 2, 2]。
- 第 43 页：3×3、stride 1 最大池化 5×5 → 3×3，九个值逐一复算（[9 9 5; 9 9 5; 8 6 9]）。
- 第 44 页：(20+1)×5 = 105。
- 第 46 页：卷积输出（除一处见下）、ReLU、max pool [7 8; 9 6]、FC 输出 [4, −1] 复算无误。
- 第 50–51 页（LeNet-5）：C1 156、C3 2416、C5 48120、F6 10164、输出层 850，尺寸链 32→28→14→10→5→1 全部正确。
- 第 52 页 ILSVRC 柱状图成绩（28.2, 25.8, 16.4, 11.7, 7.3, 6.7, 3.6, 3.0, 2.3；人类 5.1）与历届结果一致。
- 第 53 页（AlexNet）：(227−11)/4+1 = 55；(55−3)/2+1 = 27；约 60M 参数。
- 第 55 页（VGG-16）：224 → 112 → 56 的尺寸链；16 个权重层；top-5 误差 7.3%（VGG 7 模型集成，来源同上 arXiv 1409.1556）。
- 第 56 页：2 层 3×3 → RF 5×5，3 层 → 7×7，L 层 → 1+2L；7×7 约 49D² vs 3×(3×3) 约 27D² 参数。
- 第 60 页：无瓶颈 5·5·192·32 = 153,600 参数、≈120M 次乘法；有瓶颈 15,872 参数、≈12.4M 次乘法，均复算正确。
- 第 63–64 页：常规卷积 72 参数 / 1152 次乘法；深度可分离 26 参数 / 416 次乘法。
- 第 65、67、68 页：残差公式 H(x)=F(x)+x；CS231n 层模式表达式；迁移学习描述。

## 待你确认 / 未改

| 幻灯片 | 问题 | 建议 |
|---|---|---|
| 26 | 标题 `7x7 input, 3x3 filter, stride=3 ⇒ output: ???`：这是占位符还是有意的提问？正确答案是 2×2（⌊(7−3)/3⌋+1 = 2，最右列、最下行未被处理），下一页加 P=1 变 3×3 | 若是提问就保持；若不是，建议改为 `... ⇒ output: 2x2 (doesn't fit)`。未改（可能是你的教学设计） |
| 28 等 | 输出尺寸公式没有取整号：W2 = (W1+2P−F)/S + 1；当不能整除时（如第 26 页）应为 ⌊·⌋ | 建议在第 28 页加 "(round down if not an integer)"；OMML 公式页未改 |
| 46 | 嵌入图片里 (0,2) 位置卷积输出写 −3，复算为 2·1+1·0+1·(−1)+(−2)·2+1 = −2；经 ReLU 后都是 0，不影响后续结果 | 图片无法编辑；可忽略或重画 |
| 46 | SoftMax 例子用 2 的幂：[2⁴, 2⁻¹]/(2⁴+2⁻¹) = [.97, .03]；若按标准 softmax（e 为底）应为 [.993, .007]，与 L2.1 第 31 页的 softmax 定义不一致 | 建议改成 e 为底并同步改图（图中 .97/.03），或加一句 "(base 2 for simplicity)" |
| 51 | 引用 `L4.2 “Turning FC layer into CONV Layers”` 在现有各讲稿中查不到：L4.2 现在是 "Adversarial Attacks for AD"；L4 第 41 页是 "Fully Convolutional Network (FCN)"，但内容不同 | 请告知应指向哪里再改 |
| 53 | "Introduced ReLU activation function"：ReLU 早于 AlexNet（如 Nair & Hinton 2010），AlexNet 是在大规模 CNN 中推广它 | 建议 "Popularized ReLU"；未改 |
| 61 | "12x less params (only 5M, due to no FC layers)"：论文自述比 AlexNet 少 12 倍；但本页表格参数列相加约 6.8M（含 1000K 的线性层），也并非 "no FC layers" | 建议改为 "~12x fewer params (5–7M)" 或去掉括注；未改 |
| 50 | LeNet-5 表是简化版：C3 按全连接计算 2416 参数；原论文 C3 为稀疏连接（1,516 参数），S2/S4 带可训练系数 | 作为教学简化可保留，建议加一句脚注 |
| 66 | 标题 "Deeper Nets have Better Performance"，图（ResNet 论文的 CIFAR-10 实验）实际显示：plain 网络越深越差，ResNet 才越深越好 | 建议标题改为 "Deeper ResNets have Better Performance (plain nets do not)"；未改 |
| 39、20、1、38（讲稿） | 第 39 页（Outline）讲稿是无关内容 "Safety plan / The safety plan gives an overview..."；第 20 页讲稿 `Conv4.state_dict()weight 0 0`；第 1 页讲稿是 transposed conv 的链接；第 38 页 "Two different ways" | 均为遗留，建议删除或移到对应页；按要求未动 |
| 全局 | 内容止于 ResNet（2015）；2026 年的"知名 CNN 架构"部分可考虑补 EfficientNet / ConvNeXt 以及 Vision Transformer 的对比（本讲稿未涉及 ViT） | 教学取舍，未改；L2.1 第 93 页已有 Transformer 简介 |
| 3、10 | "complex ML/DL algorithms, which may sometimes be unreliable and unpredictable" 及 "deep learning revolution ... over a decade ago"（2012 → 2026 约 14 年，仍成立） | 无需改，仅记录 |

## PDF 过期提醒

`L3 Convolutional Neural Networks.pdf`（2026-10-07 15:14）早于现在的 pptx，已不含本次 7 处修改，需要重新导出（请在 PowerPoint 中导出，以避免 Fallback 旧图问题）。
