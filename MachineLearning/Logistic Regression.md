# 逻辑回归
$$p_{predict} = \sigma (\theta^T  X_b ) = \frac{1}{1+e^{-\theta^T X_b}}$$

# 损失函数
$$cost = -ylog(p_{predict}) - (1-y)log(1-y_{predict})$$
$$J(\theta) =\frac{ \sum y^{(i)}log(p_{predict}^{(i)}) + (1 - y^{(i)})log(1 - p_{predict}^{(i)} }{-m}$$
$$p_{predict} = \sigma (\theta^T  X_b ) = \frac{1}{1+e^{-\theta^T X_b}}$$
$$J(\theta) =\frac{ \sum y^{(i)}log(\sigma (X_b^{(i)}\theta))^{(i)}) + (1 - y^{(i)})log(1 - \sigma (X_b^{(i)}\theta) }{-m}$$
