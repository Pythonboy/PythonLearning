# PCA(主成分分析）
```
class sklearn.decomposition.PCA(n_components=None, copy=True, whiten=False, svd_solver=’auto’, tol=0.0, iterated_power=’auto’, random_state=None)
```

# Parameters
![31](https://github.com/Pythonboy/Image/blob/master/SK/31.jpg?raw=true)

# Attributes
![32](https://github.com/Pythonboy/Image/blob/master/SK/32.jpg?raw=true)
![33](https://github.com/Pythonboy/Image/blob/master/SK/33.jpg?raw=true)

# Examples
```
>>> import numpy as np
>>> from sklearn.decomposition import PCA
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> pca = PCA(n_components=2)
>>> pca.fit(X)
PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)
>>> print(pca.explained_variance_ratio_)  
[0.9924... 0.0075...]
>>> print(pca.singular_values_)  
[6.30061... 0.54980...]
```

```
>>> pca = PCA(n_components=2, svd_solver='full')
>>> pca.fit(X)                 
PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
  svd_solver='full', tol=0.0, whiten=False)
>>> print(pca.explained_variance_ratio_)  
[0.9924... 0.00755...]
>>> print(pca.singular_values_)  
[6.30061... 0.54980...]
```

```
>>> pca = PCA(n_components=1, svd_solver='arpack')
>>> pca.fit(X)
PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='arpack', tol=0.0, whiten=False)
>>> print(pca.explained_variance_ratio_)  
[0.99244...]
>>> print(pca.singular_values_)  
[6.30061...]
```

# Methods
|方法|用途|
|:-:|:-:|
|fit(X[, y])|	Fit the model with X.|
|fit_transform(X[, y])|	Fit the model with X and apply the dimensionality reduction on X.|
|get_covariance()|	Compute data covariance with the generative model.|
|get_params([deep])|	Get parameters for this estimator.|
|get_precision()|	Compute data precision matrix with the generative model.|
|inverse_transform(X)|	Transform data back to its original space.|
|score(X[, y])|	Return the average log-likelihood of all samples.|
|score_samples(X)|	Return the log-likelihood of each sample.|
|set_params(**params)|	Set the parameters of this estimator.|
|transform(X)|	Apply dimensionality reduction to X.|

```
__init__(n_components=None, copy=True, whiten=False, svd_solver=’auto’, tol=0.0, iterated_power=’auto’, random_state=None)
```

```
fit(X, y=None)
```
**Fit the model with X.**            
- Parameters:	            
**X : array-like, shape (n_samples, n_features)**               
Training data, where n_samples is the number of samples and n_features is the number of features.                 
y : Ignored
- Returns:	                  
self : object           
Returns the instance itself.         

```
fit_transform(X, y=None)
```
**Fit the model with X and apply the dimensionality reduction on X.**            

- Parameters:	              
**X : array-like, shape (n_samples, n_features)**                
Training data, where n_samples is the number of samples and n_features is the number of features. 
y : Ignored                 
- Returns:	                 
X_new : array-like, shape (n_samples, n_components)

```
get_covariance()
```
**Compute data covariance with the generative model.**        
- Returns:	                             
**cov : array, shape=(n_features, n_features)**                  
Estimated covariance of data.            

```
get_params(deep=True)
```
**Get parameters for this estimator.**      
- Parameters:	               
**deep : boolean, optional**                
If True, will return the parameters for this estimator and contained subobjects that are estimators.

- Returns:	                   
**params : mapping of string to any**
Parameter names mapped to their values.

```
inverse_transform(X)
```
**Transform data back to its original space.
In other words, return an input X_original whose transform would be X.**

- Parameters:	               
**X : array-like, shape (n_samples, n_components)**        
New data, where n_samples is the number of samples and n_components is the number of components.

- Returns:	         
X_original array-like, shape (n_samples, n_features)

```
score(X, y=None)
```
- Parameters:	            
**X : array, shape(n_samples, n_features)**              
The data.
y : Ignored
- Returns:	
**ll : float**
Average log-likelihood of the samples under the current model

```
transform(X)
```
**Apply dimensionality reduction to X.
X is projected on the first principal components previously extracted from a training set.**

- Parameters:	                   
**X : array-like, shape (n_samples, n_features)**
New data, where n_samples is the number of samples and n_features is the number of features.

- Returns:	                  
X_new : array-like, shape (n_samples, n_components)

```
>>> import numpy as np
>>> from sklearn.decomposition import IncrementalPCA
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> ipca = IncrementalPCA(n_components=2, batch_size=3)
>>> ipca.fit(X)
IncrementalPCA(batch_size=3, copy=True, n_components=2, whiten=False)
>>> ipca.transform(X) 
```

