# sklearn.scatterplot

**Draw a scatter plot with possibility of several semantic groupings.**

```python
seaborn.scatterplot(x=None, y=None, hue=None, style=None, size=None, data=None, palette=None, hue_order=None, hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=True, style_order=None, x_bins=None, y_bins=None, units=None, estimator=None, ci=95, n_boot=1000, alpha='auto', x_jitter=None, y_jitter=None, legend='brief', ax=None, **kwargs)
```

The relationship between `x` and `y` can be shown for different subsets of the data using the `hue`, `size`, and `style`parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both `hue` and `style` for the same variable) can be helpful for making graphics more accessible.



# Parameters

- **x , y** : names of variables in `data` or vector data, optional

> Input data variables; must be numeric. Can pass data directly or reference columns in `data`.

- **hue** : name of variables in `data` or vector data, optional

> Grouping variable that will produce points with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.

- size : name of variables in `data` or vector data, optional

>Grouping variable that will produce points with different sizes. Can be either categorical or numeric, although size mapping will behave differently in latter case.

- style : name of variables in `data` or vector data, optional

> Grouping variable that will produce points with different markers. Can have a numeric dtype but will always be treated as categorical.

- **data** : DataFrame

> Tidy (“long-form”) dataframe where each column is a variable and each row is an observation.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable.

- sizes :  list, dict, or tuple, optional

> An object that determines how sizes are chosen when `size` is used.

- **markers** : boolean, list, or dictionary, optional

> Object determining how to draw the markers for different levels of the `style` variable. 

- **alpha** : float

> Proportional opacity of the points.

- **legend** : “brief”, “full”, or False, optional

> How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If `False`, no legend data is added and no legend is drawn.















