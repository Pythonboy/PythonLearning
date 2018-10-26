# seaborn.pointplot

```python
seaborn.pointplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, estimator=<function mean>, ci=95, n_boot=1000, units=None, markers='o', linestyles='-', dodge=False, join=True, scale=1, orient=None, color=None, palette=None, errwidth=None, capsize=None, ax=None, **kwargs)
```

**Show point estimates and confidence intervals using scatter plot glyphs.**



# Parameters

- **x, y, hue** : names of variables in `data` or vector data, optional

> Inputs for plotting long-form data. See examples for interpretation.

- **data** : DataFrame, array, or list of arrays, optional

> Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

- **order, hue_order** : lists of strings, optional

> Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.

- **ci** : float or “sd” or None, optional

> Size of confidence intervals to draw around estimated values. If “sd”, skip bootstrapping and draw the standard deviation of the observations. If `None`, no bootstrapping will be performed, and error bars will not be drawn.

- **markers** : string or list of strings, optional

> Markers to use for each of the `hue` levels.

- **linestyles** : string or list of strings, optional

> Line styles to use for each of the `hue` levels.

- **join** : bool, optional

> If `True`, lines will be drawn between point estimates at the same `hue` level.

- **scale** : float, optional

> Scale factor for the plot elements.

- **orient** : “v” | “h”, optional

> Orientation of the plot (vertical or horizontal). This is usually inferred from the dtype of the input variables, but can be used to specify when the “categorical” variable is a numeric or when plotting wide-form data.

- **color** : matplotlib color, optional

> Color for all of the elements, or seed for a gradient palette.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette), or a dictionary mapping hue levels to matplotlib colors.