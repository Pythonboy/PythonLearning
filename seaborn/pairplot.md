# seaborn.pairplot

**Plot pairwise relationships in a dataset.**

```python
seaborn.pairplot(data, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='auto', markers=None, height=2.5, aspect=1, dropna=True, plot_kws=None, diag_kws=None, grid_kws=None, size=None)
```



# Parameters

- **data** : DataFrame

> Tidy (long-form) dataframe where each column is a variable and each row is an observation.

- **hue** : string (variable name), optional

> Variable in `data` to map plot aspects to different colors.

- **hue_order** : list of strings

> Order for the levels of the hue variable in the palette

- **palette** : dict or seaborn color palette

> Set of colors for mapping the `hue` variable. If a dict, keys should be values in the `hue`variable.

- **vars** : list of variable names, optional

> Variables within `data` to use, otherwise use every column with a numeric datatype.

- **{x, y}_vars** : lists of variable names, optional

> Variables within `data` to use separately for the rows and columns of the figure; i.e. to make a non-square plot.

- **kind** : {‘scatter’, ‘reg’}, optional

> Kind of plot for the non-identity relationships.

- **diag_kind** : {‘auto’, ‘hist’, ‘kde’}, optional

> Kind of plot for the diagonal subplots. The default depends on whether `"hue"` is used or not.

- **markers** : single matplotlib marker code or list, optional

> Either the marker to use for all datapoints or a list of markers with a length the same as the number of levels in the hue variable so that differently colored points will also have different scatterplot markers.

- **height** : scalar, optional

> Height (in inches) of each facet.

- **aspect** : scalar, optional

> Aspect * height gives the width (in inches) of each facet.

- **dropna** : boolean, optional

> Drop missing values from the data before plotting.









