# sklearn.pipeline.make_pipeline
```
sklearn.pipeline.make_pipeline(*steps, **kwargs)
```
Construct a Pipeline from the given estimators.

This is a shorthand for the Pipeline constructor; it does not require, and does not permit, naming the estimators.
Instead, their names will be set to the lowercase of their types automatically.


- Parameters:	           
**steps : list of estimators.**                  
memory : None, str or object with the joblib.Memory interface, optional                         
Used to cache the fitted transformers of the pipeline. By default, no caching is performed. If a string is given,
it is the path to the caching directory. Enabling caching triggers a clone of the transformers before fitting.
Therefore, the transformer instance given to the pipeline cannot be inspected directly. Use the attribute 
named_steps or steps to inspect estimators within the pipeline. Caching the transformers is advantageous when 
fitting is time consuming.

- Returns:	            
p : Pipeline         

# Examples
```
>>> from sklearn.naive_bayes import GaussianNB
>>> from sklearn.preprocessing import StandardScaler
>>> make_pipeline(StandardScaler(), GaussianNB(priors=None))
...     
Pipeline(memory=None,
         steps=[('standardscaler',
                 StandardScaler(copy=True, with_mean=True, with_std=True)),
                ('gaussiannb',
                 GaussianNB(priors=None, var_smoothing=1e-09))])
```






