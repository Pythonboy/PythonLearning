# sklearn.lineplot

**Draw a line plot with possibility of several semantic groupings.**

```python
seaborn.lineplot(x=None, y=None, hue=None, size=None, style=None, data=None, palette=None, hue_order=None, hue_norm=None, sizes=None, size_order=None, size_norm=None, dashes=True, markers=None, style_order=None, units=None, estimator='mean', ci=95, n_boot=1000, sort=True, err_style='band', err_kws=None, legend='brief', ax=None, **kwargs)
```

The relationship between `x` and `y` can be shown for different subsets of the data using the `hue`, `size`, and `style`parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both `hue` and `style` for the same variable) can be helpful for making graphics more accessible.

# Parameters

- **x , y** : names of variables in `data` or vector data, optional

> Input data variables; must be numeric. Can pass data directly or reference columns in `data`.

- **hue** : name of variables in `data` or vector data, optional

> Grouping variable that will produce lines with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.

- **size** : name of variables in `data` or vector data, optional

> Grouping variable that will produce lines with different widths. Can be either categorical or numeric, although size mapping will behave differently in latter case.

- **style** : name of variables in `data` or vector data, optional

> Grouping variable that will produce lines with different dashes and/or markers. Can have a numeric dtype but will always be treated as categorical.

- **data** : DataFrame

> Tidy (“long-form”) dataframe where each column is a variable and each row is an observation.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable.

- **sizes** : list, dict, or tuple, optional

> An object that determines how sizes are chosen when `size` is used

- **dashes** : boolean, list, or dictionary, optional

> Object determining how to draw the lines for different levels of the `style` variable. Setting to `True` will use default dash codes, or you can pass a list of dash codes or a dictionary mapping levels of the `style` variable to dash codes. Setting to `False` will use solid lines for all subsets. Dashes are specified as in matplotlib: a tuple of `(segment,gap)` lengths, or an empty string to draw a solid line.

- **markers** : boolean, list, or dictionary, optional

> Object determining how to draw the markers for different levels of the `style` variable. Setting to `True` will use default markers, or you can pass a list of markers or a dictionary mapping levels of the `style` variable to markers. Setting to `False` will draw marker-less lines. Markers are specified as in matplotlib.

- **legend** : “brief”, “full”, or False, optional

> How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If `False`, no legend data is added and no legend is drawn.

- **sort** : boolean, optional

> If True, the data will be sorted by the x and y variables, otherwise lines will connect points in the order they appear in the dataset.

- **ci** : int or “sd” or None, optional

> Size of the confidence interval to draw when aggregating with an estimator. “sd” means to draw the standard deviation of the data. Setting to `None` will skip bootstrapping.











































