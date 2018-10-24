# sklearn.svm.LinearSVR

```python
class sklearn.svm.LinearSVR(epsilon=0.0, tol=0.0001, C=1.0, loss=’epsilon_insensitive’, fit_intercept=True, intercept_scaling=1.0, dual=True, verbose=0, random_state=None, max_iter=1000)
```

**Linear Support Vector Regression.**

Similar to SVR with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.

This class supports both dense and sparse input.



# Parameters

![70](https://github.com/Pythonboy/Image/blob/master/SK/70.jpg?raw=true)



# Examples

```python
>>> from sklearn.svm import LinearSVR
>>> from sklearn.datasets import make_regression
>>> X, y = make_regression(n_features=4, random_state=0)
>>> regr = LinearSVR(random_state=0, tol=1e-5)
>>> regr.fit(X, y)
LinearSVR(C=1.0, dual=True, epsilon=0.0, fit_intercept=True,
     intercept_scaling=1.0, loss='epsilon_insensitive', max_iter=1000,
     random_state=0, tol=1e-05, verbose=0)
>>> print(regr.coef_)
[16.35... 26.91... 42.30... 60.47...]
>>> print(regr.intercept_)
[-4.29...]
>>> print(regr.predict([[0, 0, 0, 0]]))
[-4.29...]
```



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR.fit)(X, y[, sample_weight]) | Fit the model according to the given training data.          |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR.get_params)([deep]) | Get parameters for this estimator.                           |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR.predict)(X) | Predict using the linear model                               |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR.score)(X, y[, sample_weight]) | Returns the coefficient of determination R^2 of the prediction. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR.set_params)(**params) | Set the parameters of this estimator.                        |

