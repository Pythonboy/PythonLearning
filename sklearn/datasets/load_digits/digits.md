# 手写数字集
```
sklearn.datasets.load_digits(n_class=10, return_X_y=False)
```
| | |
|:-:|:-:|
|Classes|	10|
|Samples per| class	~180|
|Samples total|	1797|
|Dimensionality|	64|
|Features	integers| 0-16|

## Parameters
- **n_class : integer, between 0 and 10, optional (default=10)**           
The number of classes to return.
- **return_X_y : boolean, default=False.**        
If True, returns (data, target) instead of a Bunch object. See below for more information about the data and target object.


## Returns  
- **data : Bunch**   
1. **data** :  the data to learn
2. **image** : the images corresponding to each sample
3. **target** : the classification labels for each sample
4. **target_names** :  the meaning of the labels
5. **DESCR** : the full description of the dataset
- **(data, target) : tuple if return_X_y is True**

## Example
```
>>> from sklearn.datasets import load_digits
>>> digits = load_digits()
>>> print(digits.data.shape)
(1797, 64)
>>> import matplotlib.pyplot as plt 
>>> plt.gray() 
>>> plt.matshow(digits.images[0]) 
>>> plt.show() 
```








