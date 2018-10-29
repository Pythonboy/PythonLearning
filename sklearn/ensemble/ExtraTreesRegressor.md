# sklearn.ensemble.ExtraTreesRegressor

```python
class sklearn.ensemble.ExtraTreesRegressor(n_estimators=’warn’, criterion=’mse’, max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=’auto’, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, bootstrap=False, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False)
```

**An extra-trees regressor.**

This class implements a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

# Parameters & Attributes

![84](https://github.com/Pythonboy/Image/blob/master/SK/a1.jpg?raw=true)

![84](https://github.com/Pythonboy/Image/blob/master/SK/a2.jpg?raw=true)

![84](https://github.com/Pythonboy/Image/blob/master/SK/a3.jpg?raw=true)



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`apply`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor.apply)(X) | Apply trees in the forest to X, return leaf indices.         |
| [`decision_path`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor.decision_path)(X) | Return the decision path in the forest                       |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor.fit)(X, y[, sample_weight]) | Build a forest of trees from the training set (X, y).        |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor.get_params)([deep]) | Get parameters for this estimator.                           |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor.predict)(X) | Predict regression target for X.                             |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor.score)(X, y[, sample_weight]) | Returns the coefficient of determination R^2 of the prediction. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor.set_params)(**params) | Set the parameters of this estimator.                        |