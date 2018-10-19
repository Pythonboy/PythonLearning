# sklearn.preprocessing.PolynomiaFeatures
```
class sklearn.preprocessing.PolynomialFeatures(degree=2, interaction_only=False, include_bias=True)
```
Generate polynomial and interaction features.

Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or 
equal to the specified degree. **For example, if an input sample is two dimensional and of the form [a, b], the 
degree-2 polynomial features are [1, a, b, a^2, ab, b^2].**

# Parameters & Attributes
![35](https://github.com/Pythonboy/Image/blob/master/SK/35.jpg?raw=true)

# Example
```
>>> X = np.arange(6).reshape(3, 2)
>>> X
array([[0, 1],
       [2, 3],
       [4, 5]])
>>> poly = PolynomialFeatures(2)
>>> poly.fit_transform(X)
array([[ 1.,  0.,  1.,  0.,  0.,  1.],
       [ 1.,  2.,  3.,  4.,  6.,  9.],
       [ 1.,  4.,  5., 16., 20., 25.]])
>>> poly = PolynomialFeatures(interaction_only=True)
>>> poly.fit_transform(X)
array([[ 1.,  0.,  1.,  0.],
       [ 1.,  2.,  3.,  6.],
       [ 1.,  4.,  5., 20.]])
```

# Methods
|方法|用途|
|:-:|:-:|
|fit(X[, y])|	Compute number of output features.|
|fit_transform(X[, y])|	Fit to data, then transform it.|
|get_feature_names([input_features])|	Return feature names for output features|
|get_params([deep])|	Get parameters for this estimator.|
|set_params(**params)|	Set the parameters of this estimator.|
|transform(X)|	Transform data to polynomial features|











