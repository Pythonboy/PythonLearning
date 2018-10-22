# sklearn.multiclass.OneVsOneClassifier
```
class sklearn.multiclass.OneVsOneClassifier(estimator, n_jobs=None)
```
**解决二分类器的多分类问题**

# Parameters
- estimator : estimator object;
An estimator object implementing fit and one of decision_function or predict_proba.

- n_jobs : int or None, optional (default=None);
The number of jobs to use for the computation

# Attributes
- estimators_ : list of n_classes * (n_classes - 1) / 2 estimators ; 
Estimators used for predictions.

- classes_ : numpy array of shape [n_classes];
Array containing labels.

# Methods
|方法|用途|
|:-:|:-:|
|decision_function(X)|	Decision function for the OneVsOneClassifier.|
|fit(X, y)	|Fit underlying estimators.|
|get_params([deep])|	Get parameters for this estimator.|
|partial_fit(X, y[, classes])	|Partially fit underlying estimators|
|predict(X)|	Estimate the best class label for each sample in X.|
|score(X, y[, sample_weight])	|Returns the mean accuracy on the given test data and labels.|
|set_params(**params)|	Set the parameters of this estimator.|
