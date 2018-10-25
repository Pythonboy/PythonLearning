# seaborn.clustermap

**Plot a matrix dataset as a hierarchically-clustered heatmap**

```python
seaborn.clustermap(data, pivot_kws=None, method='average', metric='euclidean', z_score=None, standard_scale=None, figsize=None, cbar_kws=None, row_cluster=True, col_cluster=True, row_linkage=None, col_linkage=None, row_colors=None, col_colors=None, mask=None, **kwargs)
```



# Parameters

- **data: 2D array-like**

> Rectangular data for clustering.Cannot contain NAs.

- **pivot_kws** : dict, optional

> If data is a tidy dataframe, can provide keyword arguments for pivot to create a rectangular dataframe.

- **method** : str, optional

> Linkage method to use for calculating clusters.

- **metric** : str, optional

> Distance metric to use for the data. 

- **standard_scale** : int or None, optional

> Either 0 (rows) or 1 (columns). Whether or not to standardize that dimension, meaning for each row or column, subtract the minimum and divide each by its maximum.

- **figsize: tuple of two ints, optional**

> Size of the figure to create.

- **mask** : boolean array or DataFrame, optional

> If passed, data will not be shown in cells where `mask` is True. Cells with missing values are automatically masked. Only used for visualizing, not for calculating.

















