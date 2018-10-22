# sklearn.linear_model.Lasso
```
class sklearn.linear_model.Lasso(alpha=1.0, fit_intercept=True, normalize=False, precompute=False, copy_X=True, max_iter=1000, tol=0.0001, warm_start=False, positive=False, random_state=None, selection=’cyclic’)
```
Linear Model trained with L1 prior as regularizer (aka the Lasso)
$$(\frac{1}{2 * n_{samples}}) * ||y - Xw||^2 + alpha * ||w||$$
Technically the Lasso model is optimizing the same objective function as the Elastic Net with l1_ratio=1.0 (no L2 penalty).

# Parameters & Attributes
![46](https://github.com/Pythonboy/Image/blob/master/SK/46.jpg?raw=true)

# Examples
```
>>> from sklearn import linear_model
>>> clf = linear_model.Lasso(alpha=0.1)
>>> clf.fit([[0,0], [1, 1], [2, 2]], [0, 1, 2])
Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
   normalize=False, positive=False, precompute=False, random_state=None,
   selection='cyclic', tol=0.0001, warm_start=False)
>>> print(clf.coef_)
[0.85 0.  ]
>>> print(clf.intercept_)  
0.15...
```

# Methods
|方法|用途|
|:-:|:-:|
|fit(X, y[, check_input])|	Fit model with coordinate descent.|
|get_params([deep])|	Get parameters for this estimator.|
|path(X, y[, l1_ratio, eps, n_alphas, …])|	Compute elastic net path with coordinate descent|
|predict(X)|	Predict using the linear model|
|score(X, y[, sample_weight])|	Returns the coefficient of determination R^2 of the prediction.|
|set_params(**params)|	Set the parameters of this estimator.|



















