# sklearn.model_selection.GridSearchCV（网格搜索）
```
class sklearn.model_selection.GridSearchCV(estimator, param_grid, scoring=None, fit_params=None, n_jobs=None, iid=’warn’, refit=True, cv=’warn’, verbose=0, pre_dispatch=‘2*n_jobs’, error_score=’raise-deprecating’, return_train_score=’warn’)
```
![12](https://github.com/Pythonboy/Image/blob/master/SK/12.jpg?raw=true)

# Attributes
![3](https://github.com/Pythonboy/Image/blob/master/SK/13.jpg?raw=true)

**Example**
```
>>> from sklearn import svm, datasets
>>> from sklearn.model_selection import GridSearchCV
>>> iris = datasets.load_iris()
>>> parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
>>> svc = svm.SVC(gamma="scale")
>>> clf = GridSearchCV(svc, parameters, cv=5)
>>> clf.fit(iris.data, iris.target)
...                             
GridSearchCV(cv=5, error_score=...,
       estimator=SVC(C=1.0, cache_size=..., class_weight=..., coef0=...,
                     decision_function_shape='ovr', degree=..., gamma=...,
                     kernel='rbf', max_iter=-1, probability=False,
                     random_state=None, shrinking=True, tol=...,
                     verbose=False),
       fit_params=None, iid=..., n_jobs=None,
       param_grid=..., pre_dispatch=..., refit=..., return_train_score=...,
       scoring=..., verbose=...)
>>> sorted(clf.cv_results_.keys())
...                             
['mean_fit_time', 'mean_score_time', 'mean_test_score',...
 'mean_train_score', 'param_C', 'param_kernel', 'params',...
 'rank_test_score', 'split0_test_score',...
 'split0_train_score', 'split1_test_score', 'split1_train_score',...
 'split2_test_score', 'split2_train_score',...
 'std_fit_time', 'std_score_time', 'std_test_score', 'std_train_score'...]
```

# Methods
|方法|用途|
|:-:|:-:|
|decision_function(X)	|Call decision_function on the estimator with the best found parameters.|
|fit(X[, y, groups])|	Run fit with all sets of parameters.|
|get_params([deep])|	Get parameters for this estimator.|
|inverse_transform(Xt)|	Call inverse_transform on the estimator with the best found params.|
|predict(X)|	Call predict on the estimator with the best found parameters.|
|predict_log_proba(X)	|Call predict_log_proba on the estimator with the best found parameters.|
|predict_proba(X)	|Call predict_proba on the estimator with the best found parameters.|
|score(X[, y])|	Returns the score on the given data, if the estimator has been refit.|
|set_params(**params)	|Set the parameters of this estimator.|
|transform(X)	|Call transform on the estimator with the best found parameters.|

```
__init__(estimator, param_grid, scoring=None, fit_params=None, n_jobs=None, iid=’warn’, refit=True, cv=’warn’, verbose=0, pre_dispatch=‘2*n_jobs’, error_score=’raise-deprecating’, return_train_score=’warn’)
```

```
decision_function(X)
```
![14](https://github.com/Pythonboy/Image/blob/master/SK/14.jpg?raw=true)

```
fit(X, y=None, groups=None, **fit_params)
```
![15](https://github.com/Pythonboy/Image/blob/master/SK/15.jpg?raw=true)

```
get_params(deep=True)
```
![16](https://github.com/Pythonboy/Image/blob/master/SK/16.jpg?raw=true)


```
inverse_transform(Xt)
```
![17](https://github.com/Pythonboy/Image/blob/master/SK/17.jpg?raw=true)

```
predict(X)
```
![18](https://github.com/Pythonboy/Image/blob/master/SK/18.jpg?raw=true)

```
score(X, y=None)
```
![19](https://github.com/Pythonboy/Image/blob/master/SK/19.jpg?raw=true)
