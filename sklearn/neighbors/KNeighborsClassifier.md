# sklearn.neighbors.KNeighborsClassifier
**KNN算法： 用于分类**
```
class sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, p=2, metric=’minkowski’, metric_params=None, n_jobs=None, **kwargs)
```

## Parameters
### 1. n_neighbors
***int,optional(default = 5)***         
用于确定参考的近邻数据个数

### 2. weights
***str,optional(default = 'uniform'***          
用于预测过程中
- **uniform**: uniform weights. All points in each neighborhood are weighted equally
- **distance**: weight points by the inverse of their distance. in this case, closer neighbors of a query point will have a greater influence than neighbors which are further away

### 3. n_jobs
***int or none, optional(default = None)***
多线程（none mean 1)

### 4. metirc
***string or callable, default = "minkowski"***  
用于度量树的距离度量

### 5. p
***int,optional (default = 2)***          
闵可夫斯基度量的幂参数:
- p = 1 : 曼哈顿距离
- p = 2 ：欧拉距离

### 6. leaf_size
***int,optional(default = 30)***         
传给BallTree or KDTree的叶子数量。它会影响构建和查询的速度，以及存储树所需的内存。最优值取决于问题的性质

### 7.algorithm
***{"auto","ball_tree","kd_tree","brute"},optional***       
用于计算最近邻的算法：
- ‘ball_tree’ will use BallTree
- ‘kd_tree’ will use KDTree
- ‘brute’ will use a brute-force search.
- ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method.

## Methods
|方法|用途|
|:-:|:-:|
|fit(X, y)|	Fit the model using X as training data and y as target values|
|get_params([deep])|	Get parameters for this estimator.|
|kneighbors([X, n_neighbors, return_distance])	|Finds the K-neighbors of a point.|
|kneighbors_graph([X, n_neighbors, mode])|	Computes the (weighted) graph of k-Neighbors for points in X|
|predict(X)|	Predict the class labels for the provided data|
|predict_proba(X)	|Return probability estimates for the test data X.|
|score(X, y[, sample_weight])|	Returns the mean accuracy on the given test data and labels.|
|set_params(**params)|	Set the parameters of this estimator.|

```
__init__(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, p=2, metric=’minkowski’, metric_params=None, n_jobs=None, **kwargs)
```
### fit(X,Y)
X : ***{array-like, sparse matrix, BallTree, KDTree}***
y = ***{array-like, sparse matrix}***

### get_params(deep = True)
- parameters : deep —— boolean,optional ; If True, will return the parameters for this estimator and contained subobjects that are estimators.
- Returns : params : mapping of string to any

### predict(X)
Predict the class labels for the provided data
- Parameters : array-like, shape (n_query, n_features), or (n_query, n_indexed) if metric == ‘precomputed’
- Returns : array of shape [n_samples] or [n_samples, n_outputs]

### predict_proba(X)
Return probability estimates for the test data X.
- Parameters : array-like, shape (n_query, n_features), or (n_query, n_indexed) if metric == ‘precomputed’
- Returns : array of shape = [n_samples, n_classes], or a list of n_outputs

### score(X,y,sample_weight = None)
Returns the mean accuracy on the given test data and labels.
X : Test samples.
y : True labels for X.
sample_weight : Sample weights.

Returns : score —— float , Mean accuracy of self.predict(X) wrt. y.

### kneighbors(X=None, n_neighbors=None, return_distance=True)
***Finds the K-neighbors of a point. Returns indices of and distances to the neighbors of each point.***
- Parameters:
1. X : The query point or points. If not provided, neighbors of each indexed point are returned. In this case, the query point is not considered its own neighbor.
2. n_neighbors: int,Number of neighbors to get (default is the value passed to the constructor).
3. return_distance : boolean, optional. Defaults to True.If False, distances will not be returned
- Returns:
1. dist:array , Array representing the lengths to points, only present if return_distance=True
2. ind : array, Indices of the nearest points in the population matrix.

**Example**
*In the following example, we construct a NeighborsClassifier class from an array representing our data set and ask who’s the closest point to [1,1,1]*
```
>>> samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]
>>> from sklearn.neighbors import NearestNeighbors
>>> neigh = NearestNeighbors(n_neighbors=1)
>>> neigh.fit(samples) 
NearestNeighbors(algorithm='auto', leaf_size=30, ...)
>>> print(neigh.kneighbors([[1., 1., 1.]])) 
(array([[0.5]]), array([[2]]))
```






