# seaborn.stripplot

```python
seaborn.stripplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, jitter=True, dodge=False, orient=None, color=None, palette=None, size=5, edgecolor='gray', linewidth=0, ax=None, **kwargs)
```

**Draw a scatterplot where one variable is categorical.**

A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.



# Parameters

- **x, y, hue** : names of variables in `data` or vector data, optional

> Inputs for plotting long-form data. See examples for interpretation.

- **data** : DataFrame, array, or list of arrays, optional

> Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

- **order, hue_order** : lists of strings, optional

> Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.

- **jitter** : float, `True`/`1` is special-cased, optional

> Amount of jitter (only along the categorical axis) to apply. This can be useful when you have many points and they overlap, so that it is easier to see the distribution. 

- **orient** : “v” | “h”, optional

> Orientation of the plot (vertical or horizontal). 

- **color** : matplotlib color, optional

> Color for all of the elements, or seed for a gradient palette.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable.

- **size** : float, optional

> Diameter of the markers, in points

- **edgecolor** : matplotlib color, “gray” is special-cased, optional

> Color of the lines around each point. 

- **linewidth** : float, optional

> Width of the gray lines that frame the plot elements.