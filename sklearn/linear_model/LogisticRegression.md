# sklearn.linear_model.LogisticRegression
```
class sklearn.linear_model.LogisticRegression(penalty=’l2’, dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver=’warn’, max_iter=100, multi_class=’warn’, verbose=0, warm_start=False, n_jobs=None)
```
Logistic Regression (aka logit, MaxEnt) classifier.

In the multiclass case, the training algorithm uses the one-vs-rest (OvR) scheme if the ‘multi_class’ option is set to ‘ovr’, and uses the cross- entropy loss if the ‘multi_class’ option is set to ‘multinomial’. (Currently the ‘multinomial’ option is supported only by the ‘lbfgs’, ‘sag’ and ‘newton-cg’ solvers.)

This class implements regularized logistic regression using the ‘liblinear’ library, ‘newton-cg’, ‘sag’ and ‘lbfgs’ solvers. It can handle both dense and sparse input. Use C-ordered arrays or CSR matrices containing 64-bit floats for optimal performance; any other input format will be converted (and copied).

The ‘newton-cg’, ‘sag’, and ‘lbfgs’ solvers support only L2 regularization with primal formulation. The ‘liblinear’ solver supports both L1 and L2 regularization, with a dual formulation only for the L2 penalty.

# Parameters & Attributes
![54](https://github.com/Pythonboy/Image/blob/master/SK/54.jpg?raw=true)
![55](https://github.com/Pythonboy/Image/blob/master/SK/55.jpg?raw=true)

# Examples
```
>>> from sklearn.datasets import load_iris
>>> from sklearn.linear_model import LogisticRegression
>>> X, y = load_iris(return_X_y=True)
>>> clf = LogisticRegression(random_state=0, solver='lbfgs',
...                          multi_class='multinomial').fit(X, y)
>>> clf.predict(X[:2, :])
array([0, 0])
>>> clf.predict_proba(X[:2, :]) 
array([[9.8...e-01, 1.8...e-02, 1.4...e-08],
       [9.7...e-01, 2.8...e-02, ...e-08]])
>>> clf.score(X, y)
0.97...
```

#  Methods
|方法|用途|
|:-:|:-:|
|decision_function(X)|	Predict confidence scores for samples.|
|densify()|	Convert coefficient matrix to dense array format.|
|fit(X, y[, sample_weight])|	Fit the model according to the given training data.|
|get_params([deep])	|Get parameters for this estimator.|
|predict(X)|	Predict class labels for samples in X.|
|predict_log_proba(X)	|Log of probability estimates.|
|predict_proba(X)|	Probability estimates.|
|score(X, y[, sample_weight])|	Returns the mean accuracy on the given test data and labels.|
|set_params(**params)	|Set the parameters of this estimator.|
|sparsify()|	Convert coefficient matrix to sparse format.|
