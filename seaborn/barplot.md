# seaborn.barplot
```
seaborn.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, estimator=<function mean>, ci=95,
n_boot=1000, units=None, orient=None, color=None, palette=None, saturation=0.75, errcolor='.26', errwidth=None, capsize=None,
dodge=True, ax=None, **kwargs)¶
```

## parameters
- x,y,hue: names of variables in data or vector data, optional
- data : DataFrame, array, or list of arrays, optional,Dataset for plotting. If x and y are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.
- color : Color for all of the elements, or seed for a gradient palette.
- ax : matplotlib Axes, optional. Axes object to draw the plot onto, otherwise uses the current Axes.

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








