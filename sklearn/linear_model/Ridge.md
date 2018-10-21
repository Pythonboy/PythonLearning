# sklearn.linear_model.Ridge
```
class sklearn.linear_model.Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver=’auto’, random_state=None)
```
Linear least squares with l2 regularization.

Minimizes the objective function:
$$||y - Xw||^2_2 + alpha * ||w||^2_2$$
This model solves a regression model where the loss function is the linear least squares function and regularization is given by 
the l2-norm. Also known as Ridge Regression or Tikhonov regularization. This estimator has built-in support for multi-variate 
regression (i.e., when y is a 2d-array of shape [n_samples, n_targets]).

# Parameters & Attributes
![44](https://github.com/Pythonboy/Image/blob/master/SK/44.jpg?raw=true)
![45](https://github.com/Pythonboy/Image/blob/master/SK/45.jpg?raw=true)

# Examples
```
>>> from sklearn.linear_model import Ridge
>>> import numpy as np
>>> n_samples, n_features = 10, 5
>>> np.random.seed(0)
>>> y = np.random.randn(n_samples)
>>> X = np.random.randn(n_samples, n_features)
>>> clf = Ridge(alpha=1.0)
>>> clf.fit(X, y) 
Ridge(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=None,
      normalize=False, random_state=None, solver='auto', tol=0.001)
```

# Methods
|方法|用途|
|:-:|:-:|
|fit(X, y[, sample_weight])|	Fit Ridge regression model|
|get_params([deep])|	Get parameters for this estimator.|
|predict(X)|	Predict using the linear model|
|score(X, y[, sample_weight])|	Returns the coefficient of determination R^2 of the prediction.|
|set_params(**params)|	Set the parameters of this estimator.|

```
__init__(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver=’auto’, random_state=None)
```

```
fit(X, y, sample_weight=None)
```
Fit Ridge regression model        

- Parameters:	              
1. X : {array-like, sparse matrix}, shape = [n_samples, n_features]          
Training data  

2. y : array-like, shape = [n_samples] or [n_samples, n_targets]       
Target values       

3. sample_weight : float or numpy array of shape [n_samples]     
Individual weights for each sample       

- Returns:	           
self : returns an instance of self.       

```
get_params(deep=True)
```
Get parameters for this estimator.

- Parameters:	   
1. deep : boolean, optional
If True, will return the parameters for this estimator and contained subobjects that are estimators.

- Returns:	
1. params : mapping of string to any
Parameter names mapped to their values.

```
predict(X)
```
Predict using the linear model
- Parameters:	
1. X : array_like or sparse matrix, shape (n_samples, n_features)
Samples.

- Returns:	
1. C : array, shape (n_samples,)
Returns predicted values.

```
score(X, y, sample_weight=None)
```
Returns the coefficient of determination R^2 of the prediction.
- Parameters:	
1. X : array-like, shape = (n_samples, n_features) ; 
Test samples. For some estimators this may be a precomputed kernel matrix instead, shape = (n_samples, n_samples_fitted], where n_samples_fitted is the number of samples used in the fitting for the estimator.

2. y : array-like, shape = (n_samples) or (n_samples, n_outputs) ; 
True values for X.

3. sample_weight : array-like, shape = [n_samples], optional ; 
Sample weights.

- Returns:	
1. score : float
R^2 of self.predict(X) wrt. y.

```
set_params(**params)
```
Set the parameters of this estimator.
