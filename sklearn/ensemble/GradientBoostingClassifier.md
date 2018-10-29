# sklearn.ensemble.GradientBoostClassifier

```python
class sklearn.ensemble.GradientBoostingClassifier(loss=’deviance’, learning_rate=0.1, n_estimators=100, subsample=1.0, criterion=’friedman_mse’, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_decrease=0.0, min_impurity_split=None, init=None, random_state=None, max_features=None, verbose=0, max_leaf_nodes=None, warm_start=False, presort=’auto’, validation_fraction=0.1, n_iter_no_change=None, tol=0.0001)
```



# Parameters & Attributes

![91](https://github.com/Pythonboy/Image/blob/master/SK/91.jpg?raw=true)

![92](https://github.com/Pythonboy/Image/blob/master/SK/92.jpg?raw=true)

![93](https://github.com/Pythonboy/Image/blob/master/SK/93.jpg?raw=true)



# Methods

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`apply`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.apply)(X) | Apply trees in the ensemble to X, return leaf indices.       |
| [`decision_function`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.decision_function)(X) | Compute the decision function of `X`.                        |
| [`fit`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.fit)(X, y[, sample_weight, monitor]) | Fit the gradient boosting model.                             |
| [`get_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.get_params)([deep]) | Get parameters for this estimator.                           |
| [`predict`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict)(X) | Predict class for X.                                         |
| [`predict_log_proba`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict_log_proba)(X) | Predict class log-probabilities for X.                       |
| [`predict_proba`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.predict_proba)(X) | Predict class probabilities for X.                           |
| [`score`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.score)(X, y[, sample_weight]) | Returns the mean accuracy on the given test data and labels. |
| [`set_params`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.set_params)(**params) | Set the parameters of this estimator.                        |
| [`staged_decision_function`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_decision_function)(X) | Compute decision function of `X` for each iteration.         |
| [`staged_predict`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict)(X) | Predict class at each stage for X.                           |
| [`staged_predict_proba`](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict_proba)(X) | Predict class probabilities at each stage for X.             |