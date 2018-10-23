# seaborn.catplot

```Python
seaborn.catplot(x=None, y=None, hue=None, data=None, row=None, col=None, col_wrap=None, estimator=<function mean>, ci=95, n_boot=1000, units=None, order=None, hue_order=None, row_order=None, col_order=None, kind='strip', height=5, aspect=1, orient=None, color=None, palette=None, legend=True, legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, **kwargs)
```

The `kind` parameter selects the underlying axes-level function to use:

Categorical scatterplots:

- [`stripplot()`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot) (with `kind="strip"`; the default)
- [`swarmplot()`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot) (with `kind="swarm"`)

Categorical distribution plots:

- [`boxplot()`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot) (with `kind="box"`)
- [`violinplot()`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot) (with `kind="violin"`)
- [`boxenplot()`](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot) (with `kind="boxen"`)

Categorical estimate plots:

- [`pointplot()`](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot) (with `kind="point"`)
- [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot) (with `kind="bar"`)
- [`countplot()`](https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot) (with `kind="count"`)



# Parameters

- **X ,y ,hue **:  names of variables in `data`;Inputs for plotting long-form data

- **data** : DataFrame ; Long-form (tidy) dataset for plotting. Each column should correspond to a variable, and each row should correspond to an observation.

- **row , col** : names of variables in `data`, optional ;Categorical variables that will determine the faceting of the grid.

- **estimator** :   callable that maps vector -> scalar, optional; Statistical function to estimate within each categorical bin.

- **kind** : string, optional ; Options are: “point”, “bar”, “strip”, “swarm”, “box”, “violin”, or “boxen”.

- **height** : scalar, optional ; Height (in inches) of each facet. See also: `aspect`.

- **aspect** : Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.

- **orient** : “v” | “h”, optional

- **color** : Color for all of the elements, or seed for a gradient palette.

- **palette** : Colors to use for the different levels of the `hue` variable

- **legend** : If `True` and there is a `hue` variable, draw a legend on the plot.

- **col_wrap** : “Wrap” the column variable at this width, so that the column facets span multiple rows. 
