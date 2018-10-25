# seaborn.regplot

**Plot data and a linear regression model fit.**

```python
seaborn.regplot(x, y, data=None, x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color=None, marker='o', scatter_kws=None, line_kws=None, ax=None)
```



# Parameters

- **x, y: string, series, or vector array**

> Input variables. If strings, these should correspond with column names in `data`. When pandas objects are used, axes will be labeled with the series name.

- **data** : DataFrame

> Tidy (“long-form”) dataframe where each column is a variable and each row is an observation.

- **x_estimator** : callable that maps vector -> scalar, optional

> Apply this function to each unique value of `x` and plot the resulting estimate. This is useful when `x` is a discrete variable. If `x_ci` is given, this estimate will be bootstrapped and a confidence interval will be drawn.

- **scatter** : bool, optional

> If `True`, draw a scatterplot with the underlying observations (or the `x_estimator` values).

- **fit_reg** : bool, optional

> If `True`, estimate and plot a regression model relating the `x` and `y` variables.

- **label** : string

> Label to apply to ether the scatterplot or regression line (if `scatter` is `False`) for use in a legend.

- **color** : matplotlib color

> Color to apply to all plot elements; 

- **marker** : matplotlib marker code

> Marker to use for the scatterplot glyphs.





























