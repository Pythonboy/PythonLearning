# 数据集的处理
通过将数据集分离为测试集和训练集，从而在模型进入真实环境前改进模型

```
import numpy as np

def train_test_split(X,y,test_ratio = 0.2 , seed = None):
    assert X.shape[0] == y.shape[0];
    '''the size of X must be equal to the size of y'''
    assert 0.0<=test_ratio<=1.0;
    '''the test ratio must be valid'''
    if seed:
        np.random.seed(seed);
    n_samples = len(X);
    shuffle_index = np.random.permutation(n_samples);
    test_size = int(test_ratio * n_samples);
    test_indexes = shuffle_index[:test_size];
    train_indexes = shuffle_index[test_size:];

    X_train = X[train_indexes];
    X_test = X[test_indexes];
    y_train = y[train_indexes];
    y_test = y[test_indexes];
    return X_train,X_test,y_train,y_test;
```
