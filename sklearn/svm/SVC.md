# sklearn.svm.SVC

```python
class sklearn.svm.SVC(C=1.0, kernel=’rbf’, degree=3, gamma=’auto_deprecated’, coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=’ovr’, random_state=None)
```

**C-Support Vector Classification.**

The implementation is based on libsvm. The fit time complexity is more than quadratic with the number of samples which makes it hard to scale to dataset with more than a couple of 10000 samples.

The multiclass support is handled according to a one-vs-one scheme.

For details on the precise mathematical formulation of the provided kernel functions and how gamma, coef0 and degree affect each other, see the corresponding section in the narrative documentation: [Kernel functions](http://scikit-learn.org/stable/modules/svm.html#svm-kernels).



# Parameters & Attributes

![71](https://github.com/Pythonboy/Image/blob/master/SK/71.jpg?raw=true)

![71](https://github.com/Pythonboy/Image/blob/master/SK/72.jpg?raw=true)



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`decision_function`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.decision_function)(X) | Distance of the samples X to the separating hyperplane.      |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.fit)(X, y[, sample_weight]) | Fit the SVM model according to the given training data.      |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.get_params)([deep]) | Get parameters for this estimator.                           |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.predict)(X) | Perform classification on samples in X.                      |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.score)(X, y[, sample_weight]) | Returns the mean accuracy on the given test data and labels. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.set_params)(**params) | Set the parameters of this estimator.                        |



# Examples

```python
>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
>>> y = np.array([1, 1, 2, 2])
>>> from sklearn.svm import SVC
>>> clf = SVC(gamma='auto')
>>> clf.fit(X, y) 
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
>>> print(clf.predict([[-0.8, -1]]))
```

