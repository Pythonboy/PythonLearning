# sklearn.model_selection.cross_validate
```
sklearn.model_selection.cross_validate(estimator, X, y=None, groups=None, scoring=None, cv=’warn’, n_jobs=None, verbose=0, fit_params=None, pre_dispatch=‘2*n_jobs’, return_train_score=’warn’, return_estimator=False, error_score=’raise-deprecating’)
```
![41](https://github.com/Pythonboy/Image/blob/master/SK/41.jpg?raw=true)
![42](https://github.com/Pythonboy/Image/blob/master/SK/42.jpg?raw=true)
![43](https://github.com/Pythonboy/Image/blob/master/SK/43.jpg?raw=true)

# Examples
```
>>> from sklearn import datasets, linear_model
>>> from sklearn.model_selection import cross_validate
>>> from sklearn.metrics.scorer import make_scorer
>>> from sklearn.metrics import confusion_matrix
>>> from sklearn.svm import LinearSVC
>>> diabetes = datasets.load_diabetes()
>>> X = diabetes.data[:150]
>>> y = diabetes.target[:150]
>>> lasso = linear_model.Lasso()
```
**Single metric evaluation using cross_validate**
```
>>> cv_results = cross_validate(lasso, X, y, cv=3,
...                             return_train_score=False)
>>> sorted(cv_results.keys())                         
['fit_time', 'score_time', 'test_score']
>>> cv_results['test_score']    
array([0.33150734, 0.08022311, 0.03531764])
```
**Multiple metric evaluation using cross_validate (please refer the scoring parameter doc for more information)**
```
>>> scores = cross_validate(lasso, X, y, cv=3,
...                         scoring=('r2', 'neg_mean_squared_error'),
...                         return_train_score=True)
>>> print(scores['test_neg_mean_squared_error'])      
[-3635.5... -3573.3... -6114.7...]
>>> print(scores['train_r2'])                         
[0.28010158 0.39088426 0.22784852]
```
