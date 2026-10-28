# L2 Intro to ML.pptx 审计日志(2026-10-07)

原件备份:`PPTs/bak/audit-20261007/L2 Intro to ML.pptx`(未触碰)。
方法:提取全部 30 页文字(含 mc:AlternateContent 中的 OMML 公式)、备注、表格,LibreOffice 渲染逐页查看;所有数学内容逐项重新计算;修改直接在 slide XML 的 run 文本上做(字节级替换,其余部分与原文件逐字节相同)。幻灯片数 30 → 30。

## 摘要
- 已修改:**10 处**(分布在 6 页):拼写 5 处(含 `classier` 4 处),冗余用词 2 处,公式符号 1 处,表格标签错误 1 处,技术表述 1 处。具体见下表。
- 数学核算:softmax 例、交叉熵、混淆矩阵 1/2 的 Precision/Recall/F1/FPR/Accuracy、概率求和、XOR 真值表与网络权重、BN 公式、参数量公式均已重算,**数值全部正确**(仅发现图片中一处对数底数不一致,见待确认)。
- 本讲义不含 bias/variance 的专门公式页,也没有具体框架/工具版本号、统计数据,故无需 2026 版本更新。幻灯片间无页码交叉引用,备注(P2)与内容无矛盾。
- 待你确认/未改:**12 项**。

## 已修改清单

| 页 | 修改前 → 修改后 | 原因 | 来源 |
|---|---|---|---|
| 16 | `e.g., conswider a medical test` → `e.g., consider a medical test` | 拼写 | - |
| 17 | `the classier correctly classifies 33.3%...` → `classifier` | 拼写 | - |
| 17 | `the classier misclassifies 7.2%...` → `classifier` | 拼写 | - |
| 17 | `correct prediction 91% percent of the time` → `91% of the time` | "% percent" 冗余 | - |
| 18 | `the classier correctly classifies 0%...` → `classifier` | 拼写 | - |
| 18 | `the classier misclassifies 0%...` → `classifier` | 拼写 | - |
| 18 | `correct prediction 97% percent of the time` → `97% of the time` | "% percent" 冗余 | - |
| 19 | `Area Under the Curve (AUC) is the area under ROC (.5≤ROC≤1, ...)` 公式中 `ROC` → `AUC`,即 `(.5≤AUC≤1, since FPR≤TPR)` | 不等式夹的应是 AUC 这个数值,不是 ROC 曲线 | - |
| 20 | 二分类混淆矩阵行标签 `Pred. Pos / Neg` → 交换为 `Pred. Neg(上:FN, TN) / Pos(下:TP, FP)` | 原表 "Pred.=Pos, GT=Pos" 的格子写成 FN,与定义及 P17 的矩阵(Predicted Neg 行:FN,TN;Pos 行:TP,FP)矛盾;只交换了标签文字,单元格颜色/内容不动 | P16/P17 定义 |
| 24 | `exploit momentum, e.g., Nesterov, AdaGrad, RMSProp, Adam…` → `exploit momentum and/or adaptive learning rates, e.g., ...` | AdaGrad、RMSProp 是自适应学习率方法而非动量法;Adam 二者兼有 | 通用定义(Kingma & Ba 2015;Duchi et al. 2011) |

注:P19 的公式是 PowerPoint 原生公式;LibreOffice 渲染使用回退图片,仍显示旧的 "ROC",在 PowerPoint 中应显示为 AUC。请在 PowerPoint 里确认一眼。

## 已核实无误(未改)
- P7:σ(z)=1/(1+e^-z);P(dog|x)+P(cat|x)=1。
- P8:全连接层参数数 (N_{i-1}+1)·N_i 正确;激活函数公式(Leaky ReLU、ELU、Maxout、tanh)与图一致。
- P9:XOR 真值表 00→0, 01→1, 10→1, 11→0;网络 h1=σ(-5+10x1-10x2)(x1∧¬x2)、h2=σ(-5-10x1+10x2)(¬x1∧x2)、y=σ(-5+10h1+10h2)(OR),计算结果为 XOR。
- P12:h_θ(x)=W3 max(0,W2 max(0,W1x+b1)+b2)+b3 与 "2 层 ReLU + 1 个线性层" 一致。
- P13:softmax 与 Loss = −log softmax(h)_y = log Σexp(h_j) − h_y 推导正确;图中 −log(0.25)=1.386 为自然对数。
- P14:exp(−2.85)=0.058, exp(.86)=2.36, exp(.28)=1.32;和 3.738(用舍入后数值求和;精确值 3.744,不影响三位小数);softmax=[.016,.631,.353],和为 1;图中 W·x+b 逐行验算得 [−2.85, .86, .28]。
- P15:10 个概率之和 = 1.00。
- P16:TP/TN/FP/FN 定义;Precision=TP/(TP+FP),Recall=TP/(TP+FN)。
- P17(TP=1,FP=7,FN=2,TN=90):Precision=.125,Recall=.333,F1=2·.125·.333/(.458)=.182,FPR=7/97=.072,Accuracy=91/100=.91,全部正确。
- P18(TP=0,FP=0,FN=3,TN=97):Precision 0/0 无定义,Recall=0,FPR=0,Accuracy=.97,全部正确。
- P19:ROC 上 4 个点 (0,0),(.2,.6),(.6,.8),(.6,1.0) 单调不减;降低阈值→FPR、TPR 同升,正确。
- P22:链式法则 ∂L/∂w=∂L/∂a·∂f/∂w 等与图一致。
- P29:K=5 折,每次 1 折验证、4 折训练,正确。

## 待你确认 / 未改

| 页 | 问题 | 建议 |
|---|---|---|
| 14 | 右侧图片给出 `−log(0.353) = 0.452`,这是以 10 为底(−log10 .353 = 0.452);而 P13 公式及 P13 图 (−log 0.25 = 1.386) 均是自然对数,−ln(.353)=1.041 | 需要换图或改图中数字为 1.041(图片无法编辑);或在课上说明底数 |
| 9 | 图中 "Ouput layer" 拼写错误(图片内文字) | 换图时顺手改 |
| 6 | 符号不统一:`y=σ(z)=step(wx+b)` 用 σ 表示激活函数,括号内又写 "activation function f";另外首句说激活函数是 "nonlinear",而线性回归例子用的是 identity(线性) | 建议统一为 f 或 σ,并将 "nonlinear" 改为 "typically nonlinear" |
| 5 | 文中说 x,y,b 是向量、w 是矩阵,但例子中 y 是标量房价、w 为 1×3 行向量、b 为标量 | 建议改写为 "y is a scalar here" 之类 |
| 13 | "logits z in the last hidden layer (the penultimate layer)":logits 是最后线性层的输出,把 softmax 当作最后一层才称 penultimate | 措辞可再斟酌 |
| 13 | "Minimizing Loss amounts to maximizing the logit h_y":严格说还要压低 log Σ exp(h_j),此为简化说法 | 教学取舍,你定 |
| 18 | "it is correct ?% of the time" 的 "?" 看起来像占位符(上下文说明是 ill-defined,可能是故意的) | 如果不是故意,改为 "N/A" |
| 19 | "The worst ROC curve: FPR≡TPR, AUC=.5":这是随机分类器,并非最差(AUC<.5 的分类器反转预测即可变好) | 建议 "random classifier" |
| 23 | 公式 θ←θ−α∇θ Loss(x,y;θ) 之前说 "minimize the expected loss",梯度对象应为期望损失(或单样本/小批量损失的近似) | 如有需要补一个 E[·] 或 "estimate" |
| 25 | "Compute the empirical mean and variance independently for each dimension i=1,…m" 与图中算法冲突:图中 i=1..m 是 mini-batch 样本下标(m=批大小),不是特征维度 | 建议改为 "for each dimension, over the m samples i=1,…,m of the mini-batch" |
| 27 | 引用 "Journal of machine learning research 13.2 (2012)":JMLR 13(1):281–305(Feb 2012);正文 "Bergstra et al" 与实际 "Bergstra and Bengio" | 小问题,可不改 |
| 全局 | 参考链接(laptrinhx、towardsdatascience、javatpoint、medium/swlh、dataplusplus、GitHub t81_558、YouTube)当前环境无法访问,未能验证是否失效;来源站点较老,可能已失效 | 上课前人工点开确认 |

## PDF 过期提示
`L2 Intro to ML.pdf`(2026-09-10 14:17)早于 pptx(2026-09-22)及本次修改,需要重新导出。
