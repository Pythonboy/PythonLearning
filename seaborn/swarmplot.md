# seaborn.swarmplot

````python
seaborn.swarmplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, dodge=False, orient=None, color=None, palette=None, size=5, edgecolor='gray', linewidth=0, ax=None, **kwargs)
````

**Draw a categorical scatterplot with non-overlapping points.**

This function is similar to [`stripplot()`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot), but the points are adjusted (only along the categorical axis) so that they don’t overlap. This gives a better representation of the distribution of values, but it does not scale well to large numbers of observations. This style of plot is sometimes called a “beeswarm”.

A swarm plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.



# Parameters

- **x, y, hue** : names of variables in `data` or vector data, optional

> Inputs for plotting long-form data. See examples for interpretation.

- **data** : DataFrame, array, or list of arrays, optional

> Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

- **order, hue_order** : lists of strings, optional

> Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.

- **dodge** : bool, optional

> When using `hue` nesting, setting this to `True` will separate the strips for different hue levels along the categorical axis. Otherwise, the points for each level will be plotted in one swarm.

- **orient** : “v” | “h”, optional

> Orientation of the plot (vertical or horizontal)

- **color** : matplotlib color, optional

> Color for all of the elements, or seed for a gradient palette.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable.

- **size** : float, optional

> Diameter of the markers, in points.

- **edgecolor** : matplotlib color, “gray” is special-cased, optional

> Color of the lines around each point. If you pass `"gray"`, the brightness is determined by the color palette used for the body of the points.

- **linewidth** : float, optional

> Width of the gray lines that frame the plot elements.