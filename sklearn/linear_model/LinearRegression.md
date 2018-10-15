# 线性回归模型
```
class sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)
```

# Parameters&Attributes
![参数](https://github.com/Pythonboy/Image/blob/master/SK/1.jpg?raw=true)

# Examples
```
>>> import numpy as np
>>> from sklearn.linear_model import LinearRegression
>>> X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
>>> # y = 1 * x_0 + 2 * x_1 + 3
>>> y = np.dot(X, np.array([1, 2])) + 3
>>> reg = LinearRegression().fit(X, y)
>>> reg.score(X, y)
1.0
>>> reg.coef_
array([1., 2.])
>>> reg.intercept_ 
3.0000...
>>> reg.predict(np.array([[3, 5]]))
array([16.])
```

# Methods
|方法|用途|
|:-:|:-:|
|fit(X, y[, sample_weight])|	Fit linear model.|
|get_params([deep])|	Get parameters for this estimator.|
|predict(X)|	Predict using the linear model|
|score(X, y[, sample_weight])|	Returns the coefficient of determination R^2 of the prediction.|
|set_params(**params)|	Set the parameters of this estimator.|

```
__init__(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)
```

```
fit(X, y, sample_weight=None)
```
**fit linear model**    
![参数](https://github.com/Pythonboy/Image/blob/master/SK/2.jpg?raw=true)

```
get_params(deep=True)
```
**Get parameters for this estimator**       
- **deep : boolean, optional**    
If True, will return the parameters for this estimator and contained subobjects that are estimators.
- **Returns** : params —— mapping of string to any  
Parameter names mapped to their values

```
predict(X)
```
**Predict using the linear model**
- **X : array_like or sparse matrix, shape (n_samples, n_features)**         
Samples.
- **Returns** : C —— array, shape (n_samples,)            
Returns predicted values.

```
score(X, y, sample_weight=None)
```
**Returns the coefficient of determination $R^2$ of the prediction**
- **X : array-like, shape = (n_samples, n_features)**       
test Sample
- **y : array-like, shape = (n_samples) or (n_samples, n_outputs)**
true values for X
- **sample_weight : array-like, shape = [n_samples], optional**
_ **Returns** : float, $R^2$ of self.predict(X) wrt. y.

```
set_params(**params)
```
**Set the parameters of this estimator.**






