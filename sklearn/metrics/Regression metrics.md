# sklearn.metrics.mean_absolute_error
```
sklearn.metrics.mean_absolute_error(y_true, y_pred, sample_weight=None, multioutput=’uniform_average’)
```
![MAE](https://github.com/Pythonboy/Image/blob/master/SK/4.jpg?raw=true)

**Example**
```
>>> from sklearn.metrics import mean_absolute_error
>>> y_true = [3, -0.5, 2, 7]
>>> y_pred = [2.5, 0.0, 2, 8]
>>> mean_absolute_error(y_true, y_pred)
0.5
>>> y_true = [[0.5, 1], [-1, 1], [7, -6]]
>>> y_pred = [[0, 2], [-1, 2], [8, -5]]
>>> mean_absolute_error(y_true, y_pred)
0.75
>>> mean_absolute_error(y_true, y_pred, multioutput='raw_values')
array([0.5, 1. ])
>>> mean_absolute_error(y_true, y_pred, multioutput=[0.3, 0.7])
... 
0.85...
```
**原理：**
$$MAE = \frac{\sum \mid y_{predict} - y_{true} \mid }{n}$$


# sklearn.metrics.mean_squared_error
```
sklearn.metrics.mean_squared_error(y_true, y_pred, sample_weight=None, multioutput=’uniform_average’)
```
![MSE](https://github.com/Pythonboy/Image/blob/master/SK/5.jpg?raw=true)

**Example**
```
>>> from sklearn.metrics import mean_squared_error
>>> y_true = [3, -0.5, 2, 7]
>>> y_pred = [2.5, 0.0, 2, 8]
>>> mean_squared_error(y_true, y_pred)
0.375
>>> y_true = [[0.5, 1],[-1, 1],[7, -6]]
>>> y_pred = [[0, 2],[-1, 2],[8, -5]]
>>> mean_squared_error(y_true, y_pred)  
0.708...
>>> mean_squared_error(y_true, y_pred, multioutput='raw_values')
... 
array([0.41666667, 1.        ])
>>> mean_squared_error(y_true, y_pred, multioutput=[0.3, 0.7])
... 
0.825...
```

**原理：**
$$MSE = \frac{\sum (y_{predict} - y_{true})^2 }{n}$$

# sklearn.metrics.r2_score 
```
sklearn.metrics.r2_score(y_true, y_pred, sample_weight=None, multioutput=’uniform_average’)
```
![r2_score](https://github.com/Pythonboy/Image/blob/master/SK/6.jpg?raw=true)
**Example**
```
>>> from sklearn.metrics import r2_score
>>> y_true = [3, -0.5, 2, 7]
>>> y_pred = [2.5, 0.0, 2, 8]
>>> r2_score(y_true, y_pred)  
0.948...
>>> y_true = [[0.5, 1], [-1, 1], [7, -6]]
>>> y_pred = [[0, 2], [-1, 2], [8, -5]]
>>> r2_score(y_true, y_pred, multioutput='variance_weighted')
... 
0.938...
>>> y_true = [1,2,3]
>>> y_pred = [1,2,3]
>>> r2_score(y_true, y_pred)
1.0
>>> y_true = [1,2,3]
>>> y_pred = [2,2,2]
>>> r2_score(y_true, y_pred)
0.0
>>> y_true = [1,2,3]
>>> y_pred = [3,2,1]
>>> r2_score(y_true, y_pred)
-3.0
```
$$R^2 = 1 - \frac{MSE}{np.var(y_{true})}$$

# sklearn.metrics.median_absolute_error
```
sklearn.metrics.median_absolute_error(y_true, y_pred)
```
- **Parameters**
1. y_true : array-like of shape = (n_samples)
2. y_pred : array-like of shape = (n_samples)
- **Returns** : loss(float),A positive floating point value (the best value is 0.0).

**Example**
```
>>> from sklearn.metrics import median_absolute_error
>>> y_true = [3, -0.5, 2, 7]
>>> y_pred = [2.5, 0.0, 2, 8]
>>> median_absolute_error(y_true, y_pred)
0.5
```

# sklearn.metrics.mean_squared_log_error
```
sklearn.metrics.mean_squared_log_error(y_true, y_pred, sample_weight=None, multioutput=’uniform_average’)
```
![7](https://github.com/Pythonboy/Image/blob/master/SK/7.jpg?raw=true)

**Example**
```
>>> from sklearn.metrics import mean_squared_log_error
>>> y_true = [3, 5, 2.5, 7]
>>> y_pred = [2.5, 5, 4, 8]
>>> mean_squared_log_error(y_true, y_pred)  
0.039...
>>> y_true = [[0.5, 1], [1, 2], [7, 6]]
>>> y_pred = [[0.5, 2], [1, 2.5], [8, 8]]
>>> mean_squared_log_error(y_true, y_pred)  
0.044...
>>> mean_squared_log_error(y_true, y_pred, multioutput='raw_values')
... 
array([0.00462428, 0.08377444])
>>> mean_squared_log_error(y_true, y_pred, multioutput=[0.3, 0.7])
... 
0.060...
```
