# sklearn.metrics.accuracy_score
```
sklearn.metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)
```
**the set of labels predicted for a sample must exactly match the corresponding set of labels in y_true.**
![8](https://github.com/Pythonboy/Image/blob/master/SK/8.jpg?raw=true)

**Example**
```
>>> import numpy as np
>>> from sklearn.metrics import accuracy_score
>>> y_pred = [0, 2, 1, 3]
>>> y_true = [0, 1, 2, 3]
>>> accuracy_score(y_true, y_pred)
0.5
>>> accuracy_score(y_true, y_pred, normalize=False)
2
```

# sklearn.metrics.f1_score
```
sklearn.metrics.f1_score(y_true, y_pred, labels=None, pos_label=1, average=’binary’, sample_weight=None)
```
The F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its 
best value at 1 and worst score at 0. The relative contribution of precision and recallto the F1 score are equal.
The formula for the F1 score is:
```
F1 = 2 * (precision * recall) / (precision + recall)
```

![9](https://github.com/Pythonboy/Image/blob/master/SK/9.jpg?raw=true)


**Example**
```
>>> from sklearn.metrics import f1_score
>>> y_true = [0, 1, 2, 0, 1, 2]
>>> y_pred = [0, 2, 1, 0, 0, 1]
>>> f1_score(y_true, y_pred, average='macro')  
0.26...
>>> f1_score(y_true, y_pred, average='micro')  
0.33...
>>> f1_score(y_true, y_pred, average='weighted')  
0.26...
>>> f1_score(y_true, y_pred, average=None)
array([0.8, 0. , 0. ])
```

# sklearn.metrics.recall_score
```
sklearn.metrics.recall_score(y_true, y_pred, labels=None, pos_label=1, average=’binary’, sample_weight=None)
```
**The best value is 1 and the worst value is 0.**
![10](https://github.com/Pythonboy/Image/blob/master/SK/10.jpg?raw=true)

**Example**
```
>>> from sklearn.metrics import recall_score
>>> y_true = [0, 1, 2, 0, 1, 2]
>>> y_pred = [0, 2, 1, 0, 0, 1]
>>> recall_score(y_true, y_pred, average='macro')  
0.33...
>>> recall_score(y_true, y_pred, average='micro')  
0.33...
>>> recall_score(y_true, y_pred, average='weighted')  
0.33...
>>> recall_score(y_true, y_pred, average=None)
array([1., 0., 0.])
```

# sklearn.metrics.precision_score
```
sklearn.metrics.precision_score(y_true, y_pred, labels=None, pos_label=1, average=’binary’, sample_weight=None)
```
![11](https://github.com/Pythonboy/Image/blob/master/SK/11.jpg?raw=true)

**Example**
```
>>> from sklearn.metrics import precision_score
>>> y_true = [0, 1, 2, 0, 1, 2]
>>> y_pred = [0, 2, 1, 0, 0, 1]
>>> precision_score(y_true, y_pred, average='macro')  
0.22...
>>> precision_score(y_true, y_pred, average='micro')  
0.33...
>>> precision_score(y_true, y_pred, average='weighted')
... 
0.22...
>>> precision_score(y_true, y_pred, average=None)  
array([0.66..., 0.        , 0.        ])
```

# 对F1 score,recall,precision的解释

|H(xi)=1,yi=1|
|:-:|
|H(xi)=1,yi=0|
|H(xi)=0,yi=1|
|H(xi)=0,yi=0|
- 预测为正，实际也为正，我们称为 true positive (TP)
- 预测为正，实际为负，我们称为 false positive (FP)
- 预测为负，实际为正，称为false negative (FN)
- 预测为负，实际也为负，称为 true negative (TN)   
因此，对于一个给定的测试集，我们可以得到如下关系：
$$N_{pre} = TP + TN$$
$$N_{total} = TP + TN + FP + FN$$
如果我们定义一个测试集中，正样本个数为P, 负样本个数为N, 那么我们可以知道$P=TP+FN$,$N=TN+FP$   
所以，我们常用的识别率 acc 其实就等于 
$$Acc = \frac{TP + TN}{TP + TN + FP + FN} = \frac{TP + TN}{P + N}$$
进一步，我们可以定义recall ，precision， F1-score 如下所示：
$$Recall = \frac{TP}{TP+FN} = \frac{TP}{P}$$
$$Precision = \frac{TP}{TP+FP}$$
$$F1 = \frac{2TP}{2TP + FP + FN} = \frac{2*Precision*Recall}{Precision + Recall}$$

**recall 体现了分类模型H对正样本的识别能力，recall 越高，说明模型对正样本的识别能力越强，precision 体现了模型对负样本的区分能力
，precision越高，说明模型对负样本的区分能力越强。F1-score 是两者的综合。F1-score 越高，说明分类模型越稳健**

有时候，通过对recall 与 precision 赋予不同的权重，表示对分类模型的偏好：
$$F_{\beta} = \frac{(1+\beta^2)TP}{(1+\beta^2)TP + \beta^2FN + FP} = \frac{(1+\beta^2)*Precision*Recall }{\beta^2 * Precision + Recall }$$
**可以看到，当 β=1，那么Fβ就退回到F1了，β 其实反映了模型分类能力的偏好，β>1 的时候，precision的权重更大，为了提高Fβ，我们希望precision 越小，而recall 应该越大，说明模型更偏好于提升recall，意味着模型更看重对正样本的识别能力； 而 β<1 的时候，recall 的权重更大，因此，我们希望recall越小，而precision越大，模型更偏好于提升precision，意味着模型更看重对负样本的区分能力。**














