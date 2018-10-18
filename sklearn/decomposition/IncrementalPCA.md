# sklearn.decomposition.IncrementalPCA
```
class sklearn.decomposition.IncrementalPCA(n_components=None, whiten=False, copy=True, batch_size=None)
```
当要分解的数据集太大而无法放入内存时，增量主成分分析（IPCA）通常用作主成分分析 （PCA）的替代。IPCA使用与输入数据样本数无关的内存
量为输入数据建立低秩近似。它仍 然依赖于输入数据功能，但更改批量大小可以控制内存使用量。

# Parameters & Attributes
![34](https://github.com/Pythonboy/Image/blob/master/34.jpg?raw=true)

# Methods
|方法|用途|
|:-:|:-:|
|fit(X[, y])|	Fit the model with X, using minibatches of size batch_size.|
|fit_transform(X[, y])	|Fit to data, then transform it.|
|get_covariance()|	Compute data covariance with the generative model.|
|get_params([deep])|	Get parameters for this estimator.|
|get_precision()|	Compute data precision matrix with the generative model.|
|inverse_transform(X)|	Transform data back to its original space.|
|partial_fit(X[, y, check_input])|	Incremental fit with X.|
|set_params(**params)|	Set the parameters of this estimator.|
|transform(X)|	Apply dimensionality reduction to X.|

# Example
```
>>> import numpy as np
>>> from sklearn.decomposition import IncrementalPCA
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> ipca = IncrementalPCA(n_components=2, batch_size=3)
>>> ipca.fit(X)
IncrementalPCA(batch_size=3, copy=True, n_components=2, whiten=False)
>>> ipca.transform(X) 
```
