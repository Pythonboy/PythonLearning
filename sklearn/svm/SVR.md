# sklearn.svm.SVR

```python
class sklearn.svm.SVR(kernel=’rbf’, degree=3, gamma=’auto_deprecated’, coef0=0.0, tol=0.001, C=1.0, epsilon=0.1, shrinking=True, cache_size=200, verbose=False, max_iter=-1)
```

Epsilon-Support Vector Regression.

The free parameters in the model are C and epsilon.

The implementation is based on libsvm.



# Parameters & Attributes

![71](https://github.com/Pythonboy/Image/blob/master/SK/73.jpg?raw=true)



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR.fit)(X, y[, sample_weight]) | Fit the SVM model according to the given training data.      |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR.get_params)([deep]) | Get parameters for this estimator.                           |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR.predict)(X) | Perform regression on samples in X.                          |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR.score)(X, y[, sample_weight]) | Returns the coefficient of determination R^2 of the prediction. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR.set_params)(**params) | Set the parameters of this estimator.                        |



# Example

```python
>>> from sklearn.svm import SVR
>>> import numpy as np
>>> n_samples, n_features = 10, 5
>>> np.random.seed(0)
>>> y = np.random.randn(n_samples)
>>> X = np.random.randn(n_samples, n_features)
>>> clf = SVR(gamma='scale', C=1.0, epsilon=0.2)
>>> clf.fit(X, y) 
SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.2, gamma='scale',
    kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
```

