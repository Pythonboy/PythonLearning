# 线性回归算法 
- 解决回归问题
- 是许多强大的非线性模型的基础
- 结果具有很好的可解释性

## 简单线性回归算法的推导
**其实就是通过向量化运算和最小二乘法导出a,b**
$$a = \frac{\sum(X_i^2 - X_{mean}^2)(y_i^2 - y_{mean}^2)}{\sum(X_i^2 - X_{mean}^2)^2}$$

$$b = a \times x_{mean} + b$$

### 多元线性回归
![1](https://github.com/Pythonboy/Image/blob/master/ML/1.jpg?raw=true)
![2](https://github.com/Pythonboy/Image/blob/master/ML/2.jpg?raw=true)
![3](https://github.com/Pythonboy/Image/blob/master/ML/3.jpg?raw=true)
![4](https://github.com/Pythonboy/Image/blob/master/ML/4.jpg?raw=true)
![5](https://github.com/Pythonboy/Image/blob/master/ML/5.jpg?raw=true)
![6](https://github.com/Pythonboy/Image/blob/master/ML/6.jpg?raw=true)
![7](https://github.com/Pythonboy/Image/blob/master/ML/7.jpg?raw=true)

## 线性回归算法的评价方法
### 均方误差 MSE （Mean Square Error)
$$MSE = \frac{\sum(y_{test}^i-y_{predict}^i)^2}{m}$$

### 均方根误差 RMSE （Root Mean Squared Error)
$$RMSE = \sqrt{MSE} = \sqrt{\frac{\sum(y_{test}^i-y_{predict}^i)^2}{m}}$$

### 平方绝对误差 MAE (Mean Absolute Error)
$$MAE = \frac{\sum\mid y_{test}^i-y_{predict}^i \mid }{m}$$

### R_Squared
$$R^2 = 1 - \frac{\sum(y_{predict}^i - y_{true}^i)^2}{\sum (y_{mean} - y_{true}^i)^2} = 1 - \frac{MSE(y_{predict},y_true)}{Var(y)}$$
- $R^2<=1$
- $R^2$越大越好。当我们的预测模型不犯任何错误时，$R^2$得到最大值1
- 当我们的模型等于基准模型时，$R^2$为0
- 如果$R^2<0$，说明我们学习到的模型还不如基准模型，此时，很有可能数据集不存在任何线性关系















