# sklearn.linear_model.SGDRegressor
```
class sklearn.linear_model.SGDRegressor(loss=’squared_loss’, penalty=’l2’, alpha=0.0001, l1_ratio=0.15, 
fit_intercept=True, max_iter=None, tol=None, shuffle=True, verbose=0, epsilon=0.1, random_state=None, 
learning_rate=’invscaling’, eta0=0.01, power_t=0.25, early_stopping=False, validation_fraction=0.1, 
n_iter_no_change=5, warm_start=False, average=False, n_iter=None)
```

# Parameters & Returens
![22](https://github.com/Pythonboy/Image/blob/master/SK/22.jpg?raw=true)
![23](https://github.com/Pythonboy/Image/blob/master/SK/23.jpg?raw=true)
![24](https://github.com/Pythonboy/Image/blob/master/SK/24.jpg?raw=true)

# Examples
```
>>> import numpy as np
>>> from sklearn import linear_model
>>> n_samples, n_features = 10, 5
>>> np.random.seed(0)
>>> y = np.random.randn(n_samples)
>>> X = np.random.randn(n_samples, n_features)
>>> clf = linear_model.SGDRegressor(max_iter=1000)
>>> clf.fit(X, y)
... 
SGDRegressor(alpha=0.0001, average=False, early_stopping=False,
       epsilon=0.1, eta0=0.01, fit_intercept=True, l1_ratio=0.15,
       learning_rate='invscaling', loss='squared_loss', max_iter=1000,
       n_iter=None, n_iter_no_change=5, penalty='l2', power_t=0.25,
       random_state=None, shuffle=True, tol=None, validation_fraction=0.1,
       verbose=0, warm_start=False)
```

# Methods
|方法|用途|
|:-:|:-:|
|densify()|	Convert coefficient matrix to dense array format.|
|fit(X, y[, coef_init, intercept_init, …])|	Fit linear model with Stochastic Gradient Descent.|
|get_params([deep])|	Get parameters for this estimator.|
|partial_fit(X, y[, sample_weight])|	Fit linear model with Stochastic Gradient Descent.|
|predict(X)|	Predict using the linear model|
|score(X, y[, sample_weight])|	Returns the coefficient of determination R^2 of the prediction.|
|set_params(*args, **kwargs)| |	
|sparsify()|	Convert coefficient matrix to sparse format.|
