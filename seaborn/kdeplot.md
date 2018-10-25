# seaborn.kdeplot

**Fit and plot a univariate or bivariate kernel density estimate.**

```python
seaborn.kdeplot(data, data2=None, shade=False, vertical=False, kernel='gau', bw='scott', gridsize=100, cut=3, clip=None, legend=True, cumulative=False, shade_lowest=True, cbar=False, cbar_ax=None, cbar_kws=None, ax=None, **kwargs)
```



# Parameters

- **data** : 1d array-like

> Input data.

- **data2: 1d array-like, optional**

> Second input data. If present, a bivariate KDE will be estimated.

- **shade** : bool, optional

> If True, shade in the area under the KDE curve (or draw with filled contours when data is bivariate).

- **vertical** : bool, optional

> If True, density is on x-axis.

- **kernel** : {‘gau’ | ‘cos’ | ‘biw’ | ‘epa’ | ‘tri’ | ‘triw’ }, optional

> Code for shape of kernel to fit with. Bivariate KDE can only use gaussian kernel.

- **bw** : {‘scott’ | ‘silverman’ | scalar | pair of scalars }, optional

> Name of reference method to determine kernel size, scalar factor, or scalar for each dimension of the bivariate plot. Note that the underlying computational libraries have different interperetations for this parameter: `statsmodels` uses it directly, but `scipy`treats it as a scaling factor for the standard deviation of the data.

- **gridsize** : int, optional

> Number of discrete points in the evaluation grid.

- **legend** : bool, optional

> If True, add a legend or label the axes when possible.

- **cumulative** : bool, optional

> If True, draw the cumulative distribution estimated by the kde.



