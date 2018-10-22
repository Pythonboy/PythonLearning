# sklearn.model_selection.KFold
```
class sklearn.model_selection.KFold(n_splits=’warn’, shuffle=False, random_state=None)
```
>Provides train/test indices to split data in train/test sets. Split dataset into k consecutive folds (without shuffling by default).
>Each fold is then used once as a validation while the k - 1 remaining folds form the training set.

# Parameters
- n_splits : int, default=3;
Number of folds. Must be at least 2.

- shuffle : boolean, optional;
Whether to shuffle the data before splitting into batches.

- random_state : int, RandomState instance or None, optional, default=None; 
If int, random_state is the seed used by the random number generator; If RandomState instance, random_state is the random number generator; If None, the random number generator is the RandomState instance used by np.random. Used when shuffle == True.

# Methods
|方法|用途|
|:-:|:-:|
|get_n_splits([X, y, groups])	|Returns the number of splitting iterations in the cross-validator|
|split(X[, y, groups])	|Generate indices to split data into training and test set.|

```
__init__(n_splits=’warn’, shuffle=False, random_state=None)
```

```
get_n_splits(X=None, y=None, groups=None)
```
Returns the number of splitting iterations in the cross-validator

- Parameters:	
1. X : object;
Always ignored, exists for compatibility.

2. y : object;
Always ignored, exists for compatibility.

3. groups : object;
Always ignored, exists for compatibility.

- Returns:	
1. n_splits : int;
Returns the number of splitting iterations in the cross-validator.

```
split(X, y=None, groups=None)
```
Generate indices to split data into training and test set.
- Parameters:	
1. X : array-like, shape (n_samples, n_features);
Training data, where n_samples is the number of samples and n_features is the number of features.

2. y : array-like, shape (n_samples,);
The target variable for supervised learning problems.

3. groups : array-like, with shape (n_samples,), optional;
Group labels for the samples used while splitting the dataset into train/test set.

- Yields:	
1. train : ndarray;
The training set indices for that split.

2. test : ndarray;
The testing set indices for that split.
