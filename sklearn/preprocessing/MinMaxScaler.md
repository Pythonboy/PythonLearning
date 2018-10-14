# 最值归一化（MinMaxScaler)
```
class sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1), copy=True)
```

```
X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
X_scaled = X_std * (max - min) + min
```

## Parameters(系数）
- **feature_range : tuple (min, max), default=(0, 1)**     
Desired range of transformed data.
- **copy : boolean, optional, default True**

## Attrubuter=s(属性）
- **min_ : ndarray, shape (n_features,)**     
Per feature adjustment for minimum.
- **scale_ : ndarray, shape (n_features,)**
Per feature relative scaling of the data.
- **data_min_ : ndarray, shape (n_features,)**       
Per feature minimum seen in the data
- **data_max_ : ndarray, shape (n_features,)**
Per feature maximum seen in the data
- **data_range_ : ndarray, shape (n_features,)**
Per feature range (data_max_ - data_min_) seen in the data

**Example**
```
>>> from sklearn.preprocessing import MinMaxScaler
>>>
>>> data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
>>> scaler = MinMaxScaler()
>>> print(scaler.fit(data))
MinMaxScaler(copy=True, feature_range=(0, 1))
>>> print(scaler.data_max_)
[ 1. 18.]
>>> print(scaler.transform(data))
[[0.   0.  ]
 [0.25 0.25]
 [0.5  0.5 ]
 [1.   1.  ]]
>>> print(scaler.transform([[2, 2]]))
[[1.5 0. ]]
```

# Methods
|方法|用途|
|:-:|:-:|
|fit(X[, y])	|Compute the minimum and maximum to be used for later scaling.|
|fit_transform(X[, y])	|Fit to data, then transform it.|
|get_params([deep])|	Get parameters for this estimator.|
|inverse_transform(X)|	Undo the scaling of X according to feature_range.|
|partial_fit(X[, y])|	Online computation of min and max on X for later scaling.|
|set_params(**params)	|Set the parameters of this estimator.|
|transform(X)	|Scaling features of X according to feature_range.|

```
__init__(feature_range=(0, 1), copy=True)
```

```
fit(X, y=None)
```
- **X : array-like, shape [n_samples, n_features]**

```
fit_transform(X, y=None, **fit_params)
```
Fit to data, then transform it.
Fits transformer to X and y with optional parameters fit_params and returns a transformed version of X.
- **Parameters**:
1. **X : numpy array of shape [n_samples, n_features]**      
Training set.
2. **y : numpy array of shape [n_samples]**         
Target values.

- **Returns**
1. **X_new : numpy array of shape [n_samples, n_features_new]**          
Transformed array.

```
get_params(deep=True)
```
- **Parameters** : 
**deep : boolean, optional**     
If True, will return the parameters for this estimator and contained subobjects that are estimators.
- **Returns**
**params : mapping of string to any**           
Parameter names mapped to their values.

```
transform(X)
```
Scaling features of X according to feature_range.
- **Parameters**
**X : array-like, shape [n_samples, n_features]**       
Input data that will be transformed.








