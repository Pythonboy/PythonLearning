# sklearn.pipeline.FeatureUnion
```
class sklearn.pipeline.FeatureUnion(transformer_list, n_jobs=None, transformer_weights=None)
```

# Parameters
- **transformer_list : list of (string, transformer) tuples**          
List of transformer objects to be applied to the data. The first half of each tuple is the name of the transformer.
- **n_jobs : int or None, optional (default=None)**       
Number of jobs to run in parallel. 
- **transformer_weights : dict, optional**
Multiplicative weights for features per transformer. Keys are transformer names, values the weights.

# Examples
```
>>> from sklearn.pipeline import FeatureUnion
>>> from sklearn.decomposition import PCA, TruncatedSVD
>>> union = FeatureUnion([("pca", PCA(n_components=1)),
...                       ("svd", TruncatedSVD(n_components=2))])
>>> X = [[0., 1., 3], [2., 2., 5]]
>>> union.fit_transform(X)    
array([[ 1.5       ,  3.0...,  0.8...],
       [-1.5       ,  5.7..., -0.4...]])
```

# Methods
|方法|用途|
|:-:|:-:|
|fit(X[, y])|	Fit all transformers using X.|
|fit_transform(X[, y])|	Fit all transformers, transform the data and concatenate results.|
|get_feature_names()|	Get feature names from all transformers.|
|get_params([deep])|	Get parameters for this estimator.|
|set_params(**kwargs)	|Set the parameters of this estimator.|
|transform(X)|	Transform X separately by each transformer, concatenate results.|




