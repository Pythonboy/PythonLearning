# 均值方差归一化（StandardScaler)
```
class sklearn.preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True)
```

## 系数（Parameters)
- **copy : optional,default True**       

- **with_mean : boolean, True by default**        
If True, center the data before scaling. 

- **with_std : boolean, True by default**      
If True, scale the data to unit variance (or equivalently, unit standard deviation).

## 属性(Attributes)      
- **scale_ : ndarray or None, shape (n_features,)**      
Per feature relative scaling of the data. Equal to None when with_std=False.

- **mean_ : ndarray or None, shape (n_features,)**      
The mean value for each feature in the training set. Equal to None when with_mean=False

- **var_ : ndarray or None, shape (n_features,)**   
The variance for each feature in the training set. Used to compute scale_. Equal to None when with_std=False.

- **n_samples_seen_ : int or array, shape (n_features,)**
The number of samples processed by the estimator for each feature. 

**Example**
```
>>> from sklearn.preprocessing import StandardScaler
>>> data = [[0, 0], [0, 0], [1, 1], [1, 1]]
>>> scaler = StandardScaler()
>>> print(scaler.fit(data))
StandardScaler(copy=True, with_mean=True, with_std=True)
>>> print(scaler.mean_)
[0.5 0.5]
>>> print(scaler.transform(data))
[[-1. -1.]
 [-1. -1.]
 [ 1.  1.]
 [ 1.  1.]]
>>> print(scaler.transform([[2, 2]]))
[[3. 3.]]
```

## Methods(方法）
|方法|用途|
|:-:|:-:|
|fit(X[, y])	|Compute the mean and std to be used for later scaling.|
|fit_transform(X[, y])	|Fit to data, then transform it.|
|get_params([deep])	|Get parameters for this estimator.|
|inverse_transform(X[, copy])	|Scale back the data to the original representation|
|partial_fit(X[, y])|	Online computation of mean and std on X for later scaling.|
|set_params(**params)|	Set the parameters of this estimator.|
|transform(X[, y, copy])	|Perform standardization by centering and scaling|


```
__init__(copy=True, with_mean=True, with_std=True)
```

```
fit(X, y=None)
```
- X : **{array-like, sparse matrix}, shape [n_samples, n_features]**    
The data used to compute the mean and standard deviation used for later scaling along the features axis.

```
fit_transform(X, y=None, **fit_params)
```
Fit to data, then transform it.
Fits transformer to X and y with optional parameters fit_params and returns a transformed version of X.

- **X : numpy array of shape [n_samples, n_features]**    
training set;
- **y : numpy array of shape [n_samples]**
Target values;

- Retruens: **	
X_new : numpy array of shape [n_samples, n_features_new]**       
Transformed array.

```
transform(X, y=’deprecated’, copy=None)
```
- **X : array-like, shape [n_samples, n_features]**
- **copy : bool, optional (default: None)**

```
get_params(deep=True)
```
- **deep : boolean, optional**     
If True, will return the parameters for this estimator and contained subobjects that are estimators.
- **params : mapping of string to any**     
Parameter names mapped to their values.




