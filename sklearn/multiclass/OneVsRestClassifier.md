# sklearn.multiclass.OneVsRestClassifier
```
class sklearn.multiclass.OneVsRestClassifier(estimator, n_jobs=None)
```
**可以使二分类模型实现多分类问题**   

# Parameters
- estimator : estimator object;
An estimator object implementing fit and one of decision_function or predict_proba.

- n_jobs : int or None, optional (default=None);
The number of jobs to use for the computation.

# Attributes
- estimators_ : list of n_classes estimators;
Estimators used for predictions.

- classes_ : array, shape = [n_classes];
Class labels.

- label_binarizer_ : LabelBinarizer object;
Object used to transform multiclass labels to binary labels and vice-versa.

- multilabel_ : boolean;
Whether this is a multilabel classifier

# Methods
|方法|用途|
|:-:|:-:|
|decision_function(X)|	Returns the distance of each sample from the decision boundary for each class.|
|fit(X, y)|	Fit underlying estimators.|
|get_params([deep])	|Get parameters for this estimator.|
|partial_fit(X, y[, classes])|	Partially fit underlying estimators|
|predict(X)|	Predict multi-class targets using underlying estimators.|
|predict_proba(X)	|Probability estimates.|
|score(X, y[, sample_weight])	|Returns the mean accuracy on the given test data and labels.|
|set_params(**params)	|Set the parameters of this estimator.|
