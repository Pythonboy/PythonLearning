# sklearn.svm.LinearSVC

```python
class sklearn.svm.LinearSVC(penalty=’l2’, loss=’squared_hinge’, dual=True, tol=0.0001, C=1.0, multi_class=’ovr’, fit_intercept=True, intercept_scaling=1, class_weight=None, verbose=0, random_state=None, max_iter=1000)
```

**Linear Support Vector Classification.**

Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.



# Parameters

![69](https://github.com/Pythonboy/Image/blob/master/SK/69.jpg?raw=true)



- **Attributes**
  1. **coef_** : array, shape = [n_features] if n_classes == 2 else [n_classes, n_features] ; This is only available in the case of a linear kernel.
  2. **intercept_** : array, shape = [1] if n_classes == 2 else [n_classes] ; Constants in decision function.

# Examples

```python
>>> from sklearn.svm import LinearSVC
>>> from sklearn.datasets import make_classification
>>> X, y = make_classification(n_features=4, random_state=0)
>>> clf = LinearSVC(random_state=0, tol=1e-5)
>>> clf.fit(X, y)
LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=0, tol=1e-05, verbose=0)
>>> print(clf.coef_)
[[0.085... 0.394... 0.498... 0.375...]]
>>> print(clf.intercept_)
[0.284...]
>>> print(clf.predict([[0, 0, 0, 0]]))
[1]
```



# Methods

|                             方法                             |                             用途                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| [`decision_function`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.decision_function)(X) |            Predict confidence scores for samples.            |
| [`densify`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.densify)() |      Convert coefficient matrix to dense array format.       |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.fit)(X, y[, sample_weight]) |     Fit the model according to the given training data.      |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.get_params)([deep]) |              Get parameters for this estimator.              |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.predict)(X) |            Predict class labels for samples in X.            |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.score)(X, y[, sample_weight]) | Returns the mean accuracy on the given test data and labels. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.set_params)(**params) |            Set the parameters of this estimator.             |
| [`sparsify`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.sparsify)() |         Convert coefficient matrix to sparse format.         |

