# sklearn.ensemble.BaggingClassifier

```python
class sklearn.ensemble.BaggingClassifier(base_estimator=None, n_estimators=10, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=False, oob_score=False, warm_start=False, n_jobs=None, random_state=None, verbose=0)
```



# Parameters & Attributes

![79](https://github.com/Pythonboy/Image/blob/master/SK/81.jpg?raw=true)

![79](https://github.com/Pythonboy/Image/blob/master/SK/82.jpg?raw=true)



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`decision_function`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.decision_function)(X) | Average of the decision functions of the base classifiers.   |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.fit)(X, y[, sample_weight]) | Build a Bagging ensemble of estimators from the training set (X, y). |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.get_params)([deep]) | Get parameters for this estimator.                           |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.predict)(X) | Predict class for X.                                         |
| [`predict_log_proba`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.predict_log_proba)(X) | Predict class log-probabilities for X.                       |
| [`predict_proba`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.predict_proba)(X) | Predict class probabilities for X.                           |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.score)(X, y[, sample_weight]) | Returns the mean accuracy on the given test data and labels. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier.set_params)(**params) | Set the parameters of this estimator.                        |