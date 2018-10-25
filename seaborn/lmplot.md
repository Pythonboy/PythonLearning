# seaborn.lmplot

**Plot data and regression model fits across a FacetGrid.**

```python
seaborn.lmplot(x, y, data, hue=None, col=None, row=None, palette=None, col_wrap=None, height=5, aspect=1, markers='o', sharex=True, sharey=True, hue_order=None, col_order=None, row_order=None, legend=True, legend_out=True, x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, truncate=False, x_jitter=None, y_jitter=None, scatter_kws=None, line_kws=None, size=None)
```

This function combines [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot) and [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid). It is intended as a convenient interface to fit regression models across conditional subsets of a dataset.

When thinking about how to assign variables to different facets, a general rule is that it makes sense to use `hue` for the most important comparison, followed by `col` and `row`. However, always think about your particular dataset and the goals of the visualization you are creating.



# Parameters

- **x, y** :  strings, optional

> Input variables; these should be column names in `data`.

- **data** : DataFrame

> Tidy (“long-form”) dataframe where each column is a variable and each row is an observation.

- **hue, col, row** : strings

> Variables that define subsets of the data, which will be drawn on separate facets in the grid. See the `*_order` parameters to control the order of levels of this variable.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable. 

- **col_wrap** : int, optional

> “Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a `row` facet.

- **height** : scalar, optional

> Height (in inches) of each facet. See also: `aspect`.

- **aspect** : scalar, optional

> Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.

- **markers** : matplotlib marker code or list of marker codes, optional

> Markers for the scatterplot. If a list, each marker in the list will be used for each level of the `hue` variable.

- **share{x,y}** : bool, ‘col’, or ‘row’ optional

> If true, the facets will share y axes across columns and/or x axes across rows.

- **legend** : bool, optional

> If `True` and there is a `hue` variable, add a legend.

- **legend_out** : bool, optional

> If `True`, the figure size will be extended, and the legend will be drawn outside the plot on the center right.

- **x_estimator** : callable that maps vector -> scalar, optional

>Apply this function to each unique value of `x` and plot the resulting estimate. 

- **scatter** : bool, optional

> If `True`, draw a scatterplot with the underlying observations (or the `x_estimator` values).

- **fit_reg** : bool, optional

> If `True`, estimate and plot a regression model relating the `x` and `y` variables.