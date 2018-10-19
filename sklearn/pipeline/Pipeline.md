# sklearn.pipeline.Pipeline
```
class sklearn.pipeline.Pipeline(steps, memory=None)
```

# Example
```
>>> from sklearn import svm
>>> from sklearn.datasets import samples_generator
>>> from sklearn.feature_selection import SelectKBest
>>> from sklearn.feature_selection import f_regression
>>> from sklearn.pipeline import Pipeline
>>> # generate some data to play with
>>> X, y = samples_generator.make_classification(
...     n_informative=5, n_redundant=0, random_state=42)
>>> # ANOVA SVM-C
>>> anova_filter = SelectKBest(f_regression, k=5)
>>> clf = svm.SVC(kernel='linear')
>>> anova_svm = Pipeline([('anova', anova_filter), ('svc', clf)])
>>> # You can set the parameters using the names issued
>>> # For instance, fit using a k of 10 in the SelectKBest
>>> # and a parameter 'C' of the svm
>>> anova_svm.set_params(anova__k=10, svc__C=.1).fit(X, y)
...                      
Pipeline(memory=None,
         steps=[('anova', SelectKBest(...)),
                ('svc', SVC(...))])
>>> prediction = anova_svm.predict(X)
>>> anova_svm.score(X, y)                        
0.83
>>> # getting the selected features chosen by anova_filter
>>> anova_svm.named_steps['anova'].get_support()
... 
array([False, False,  True,  True, False, False, True,  True, False,
       True,  False,  True,  True, False, True,  False, True, True,
       False, False])
>>> # Another way to get selected features chosen by anova_filter
>>> anova_svm.named_steps.anova.get_support()
... 
array([False, False,  True,  True, False, False, True,  True, False,
       True,  False,  True,  True, False, True,  False, True, True,
       False, False])
```

# Methods
|方法|用途|
|:-:|:-:|
|decision_function(X)|	Apply transforms, and decision_function of the final estimator|
|fit(X[, y])|	Fit the model|
|fit_predict(X[, y])|	Applies fit_predict of last step in pipeline after transforms.|
|fit_transform(X[, y])|	Fit the model and transform with the final estimator|
|get_params([deep])	|Get parameters for this estimator.|
|predict(X, **predict_params)|	Apply transforms to the data, and predict with the final estimator|
|predict_log_proba(X)|	Apply transforms, and predict_log_proba of the final estimator|
|predict_proba(X)|	Apply transforms, and predict_proba of the final estimator|
|score(X[, y, sample_weight])|	Apply transforms, and score with the final estimator|
|set_params(**kwargs)|	Set the parameters of this estimator.|





