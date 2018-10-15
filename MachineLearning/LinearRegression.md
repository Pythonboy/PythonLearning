# 线性回归算法 
- 解决回归问题
- 是许多强大的非线性模型的基础
- 结果具有很好的可解释性

## 简单线性回归算法的推导
**其实就是通过向量化运算和最小二乘法导出a,b**
$$a = \frac{\sum(X_i^2 - X_{mean}^2)(y_i^2 - y_{mean}^2)}{\sum(X_i^2 - X_{mean}^2)^2}$$

$$b = a \times x_{mean} + b$$

## 线性回归算法的评价方法
### 均方误差 MSE （Mean Square Error)
$$MSE = \cfrac{\sum(y_{test}^i-y_{predict}^i)^2{m}$$

### 均方根误差 RMSE （Root Mean Squared Error)
$$ RMSE = \sqrt{MSE} = \sqrt{\cfrac{\sum(y_{test}^i-y_{predict}^i)^2{m}}$$

### 平方绝对误差 MAE (Mean Absolute Error)
$$ MAE = \cfrac{\sum\midy_{test}^i-y_{predict}^i\mid}{m}$$
