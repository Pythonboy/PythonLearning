# 准确度的陷阱和混淆矩阵

- 分类准确度的问题： 对于极度偏斜的数据，只使用分类准确度是远远不够的



**混淆矩阵**（Confusion Matrix)

- 行代表真实值，列代表预测值
- TN ( True Negative) ; FP ( False Positive) ; FN ( False Negative) ; TP ( True Positive) —— 后面的字母代表预测值，前面的字母代表预测值是否正确

**Example**

| 真实\预测 | 0    | 1    |
| --------- | ---- | ---- |
| 0         | 9978 | 12   |
| 1         | 2    | 8    |



# 精准率和召回率

**精准率（查准率）**

$$precision = \frac{TP}{TP + FP}$$

*(理解：预测为正确的实例中实际为正确的比例 )*

*（注 ： 在有偏数据中，一般把1设置为我们关注的对象）*

**召回率（查全率）**

$$recall = \frac{TP}{TP + FN}$$

*（理解：在实际为正确的实例中被预测出来的比例）*

![58](https://github.com/Pythonboy/Image/blob/master/SK/58.jpg?raw=true)



# F1_score

$$\frac{1}{F1_score} = \frac{1}{2}(\frac{1}{precision} + \frac{1}{recall})$$

$$F1_score = \frac{2 * precision * recall}{precision + recall}$$

F1 score是precision和recall的调和平均值，取值范围为**[0,1]**



# Precision-Recall 的平衡

