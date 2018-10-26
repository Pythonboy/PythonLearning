# seaborn.barplot
```python
seaborn.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, estimator=<function mean>, ci=95,
n_boot=1000, units=None, orient=None, color=None, palette=None, saturation=0.75, errcolor='.26', errwidth=None, capsize=None,
dodge=True, ax=None, **kwargs)¶
```

**Show point estimates and confidence intervals as rectangular bars.**



## parameters

- **x, y, hue** : names of variables in `data` or vector data, optional

>Inputs for plotting long-form data. See examples for interpretation.

- **data** : DataFrame, array, or list of arrays, optional

> Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

- **ci** : float or “sd” or None, optional

> Size of confidence intervals to draw around estimated values. If “sd”, skip bootstrapping and draw the standard deviation of the observations. If `None`, no bootstrapping will be performed, and error bars will not be drawn.

- **orient** : “v” | “h”, optional

> Orientation of the plot (vertical or horizontal). This is usually inferred from the dtype of the input variables, but can be used to specify when the “categorical” variable is a numeric or when plotting wide-form data.

- **color** : matplotlib color, optional

> Color for all of the elements, or seed for a gradient palette.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette), or a dictionary mapping hue levels to matplotlib colors.

## Example
**Draw a set of vertical bar plots grouped by a categorical variable:**
```
>>> import seaborn as sns
>>> sns.set(style="whitegrid")
>>> tips = sns.load_dataset("tips")
>>> ax = sns.barplot(x="day", y="total_bill", data=tips)
```

**Draw a set of vertical bars with nested grouping by a two variables:**
```
>>> ax = sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
```








