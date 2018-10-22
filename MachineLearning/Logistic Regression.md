# 逻辑回归
$$p_{predict} = \sigma (\theta^T  X_b ) = \frac{1}{1+e^{-\theta^T X_b}}$$

# 损失函数
$$cost = -ylog(p_{predict}) - (1-y)log(1-y_{predict})$$
$$J(\theta) =\frac{ \sum y^{(i)}log(p_{predict}^{(i)}) + (1 - y^{(i)})log(1 - p_{predict}^{(i)} }{-m}$$
$$p_{predict} = \sigma (\theta^T  X_b ) = \frac{1}{1+e^{-\theta^T X_b}}$$
$$J(\theta) =\frac{ \sum y^{(i)}log(\sigma (X_b^{(i)}\theta))^{(i)}) + (1 - y^{(i)})log(1 - \sigma (X_b^{(i)}\theta) }{-m}$$

# 梯度下降法
![47](https://github.com/Pythonboy/Image/blob/master/SK/47.jpg?raw=true)
![48](https://github.com/Pythonboy/Image/blob/master/SK/48.jpg?raw=true)
![49](https://github.com/Pythonboy/Image/blob/master/SK/49.jpg?raw=true)
![50](https://github.com/Pythonboy/Image/blob/master/SK/50.jpg?raw=true)
![51](https://github.com/Pythonboy/Image/blob/master/SK/51.jpg?raw=true)
![52](https://github.com/Pythonboy/Image/blob/master/SK/52.jpg?raw=true)

# 决策边界
![53](https://github.com/Pythonboy/Image/blob/master/SK/53.jpg?raw=true)
