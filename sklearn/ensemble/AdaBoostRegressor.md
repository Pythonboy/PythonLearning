# sklearn.ensemble.AdaBoostRegressor

```python
class sklearn.ensemble.AdaBoostRegressor(base_estimator=None, n_estimators=50, learning_rate=1.0, loss=’linear’, random_state=None)
```

An AdaBoost regressor.

An AdaBoost  regressor is a meta-estimator that begins by fitting a regressor on the original dataset and then fits additional copies of the regressor on the same dataset but where the weights of instances are adjusted according to the error of the current prediction. As such, subsequent regressors focus more on difficult cases.



# Parameters & Attributes

![80](https://github.com/Pythonboy/Image/blob/master/SK/80.jpg?raw=true)



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.fit)(X, y[, sample_weight]) | Build a boosted regressor from the training set (X, y).      |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.get_params)([deep]) | Get parameters for this estimator.                           |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.predict)(X) | Predict regression value for X.                              |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.score)(X, y[, sample_weight]) | Returns the coefficient of determination R^2 of the prediction. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.set_params)(**params) | Set the parameters of this estimator.                        |
| [`staged_predict`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.staged_predict)(X) | Return staged predictions for X.                             |
| [`staged_score`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor.staged_score)(X, y[, sample_weight]) | Return staged scores for X, y.                               |