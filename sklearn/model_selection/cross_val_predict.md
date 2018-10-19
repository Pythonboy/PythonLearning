# sklearn.model_selection.cross_val_predict
```
sklearn.model_selection.cross_val_predict(estimator, X, y=None, groups=None, cv=’warn’, n_jobs=None, verbose=0, fit_params=None, pre_dispatch=‘2*n_jobs’, method=’predict’)
```
**Notes:**  
Generate cross-validated estimates for each input data point

It is not appropriate to pass these predictions into an evaluation metric. Use cross_validate to measure generalization error.

# Parameters & Attributes
![40](https://github.com/Pythonboy/Image/blob/master/SK/40.jpg?raw=true)

# Example
```
>>> from sklearn import datasets, linear_model
>>> from sklearn.model_selection import cross_val_predict
>>> diabetes = datasets.load_diabetes()
>>> X = diabetes.data[:150]
>>> y = diabetes.target[:150]
>>> lasso = linear_model.Lasso()
>>> y_pred = cross_val_predict(lasso, X, y, cv=3)
```
