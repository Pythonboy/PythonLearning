# 鸢尾花数据集
```
sklearn.datasets.load_iris(return_X_y=False)[source]
```
| | |
|:-:|:-:|
|Classes|	3|
|Samples per class	|50|
|Samples total	|150|
|Dimensionality	|4|
|Features	|real, positive|

- **Parameters**  
**return_X_y : boolean, default=False.**      
If True, returns (data, target) instead of a Bunch object. See below for more information about the data and target object.

- **Returns**  
**data : Bunch,Dictionary-like object**
1. **data** : the data to learn
2. **target** : the classification labels
3. **target_names** :  the meaning of the labels 
4. **feature_names** : the meaning of the features
5. **DESCR** : the full description of the dataset
6. **filename** : he physical location of iris csv dataset

- **(data, target) : tuple if return_X_y is True**

**Example**
```
>>> from sklearn.datasets import load_iris
>>> data = load_iris()
>>> data.target[[10, 25, 50]]
array([0, 0, 1])
>>> list(data.target_names)
['setosa', 'versicolor', 'virginica']
```


