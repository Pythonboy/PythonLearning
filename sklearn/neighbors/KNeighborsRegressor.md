# sklearn.neighbors.KNeighborsRegressor

```python
class sklearn.neighbors.KNeighborsRegressor(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, p=2, metric=’minkowski’, metric_params=None, n_jobs=None, **kwargs)
```

**Regression based on k-nearest neighbors**

*The target is predicted by local interpolation of the targets associated of the nearest neighbors in the training set.*



# Parameters

![60](https://github.com/Pythonboy/Image/blob/master/SK/60.jpg?raw=true)



# Examples

```python
>>> X = [[0], [1], [2], [3]]
>>> y = [0, 0, 1, 1]
>>> from sklearn.neighbors import KNeighborsRegressor
>>> neigh = KNeighborsRegressor(n_neighbors=2)
>>> neigh.fit(X, y) 
KNeighborsRegressor(...)
>>> print(neigh.predict([[1.5]]))
[0.5]
```



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.fit)(X, y) | Fit the model using X as training data and y as target values |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.get_params)([deep]) | Get parameters for this estimator.                           |
| [`kneighbors`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.kneighbors)([X, n_neighbors, return_distance]) | Finds the K-neighbors of a point.                            |
| [`kneighbors_graph`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.kneighbors_graph)([X, n_neighbors, mode]) | Computes the (weighted) graph of k-Neighbors for points in X |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.predict)(X) | Predict the target for the provided data                     |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.score)(X, y[, sample_weight]) | Returns the coefficient of determination R^2 of the prediction. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.set_params)(**params) | Set the parameters of this estimator.                        |