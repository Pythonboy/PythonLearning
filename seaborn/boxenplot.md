# seaborn.boxenplot

```python
seaborn.boxenplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, width=0.8, dodge=True, k_depth='proportion', linewidth=None, scale='exponential', outlier_prop=None, ax=None, **kwargs)¶
```

**Draw an enhanced box plot for larger datasets.**



# Parameters

- **x, y, hue** : names of variables in `data` or vector data, optional

> Inputs for plotting long-form data. See examples for interpretation.

- **data** : DataFrame, array, or list of arrays, optional

> Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

- **order, hue_order** : lists of strings, optional

> Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.

- **orient** : “v” | “h”, optional

> Orientation of the plot (vertical or horizontal)

- **color** : matplotlib color, optional

> Color for all of the elements, or seed for a gradient palette.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable.

- **saturation** : float, optional

> Proportion of the original saturation to draw colors at. Large patches often look better with slightly desaturated colors, but set this to `1` if you want the plot colors to perfectly match the input color spec.

- **width** : float, optional

> Width of a full element when not using hue nesting, or width of all the elements for one level of the major grouping variable.

- **dodge** : bool, optional

> When hue nesting is used, whether elements should be shifted along the categorical axis.

- **linewidth** : float, optional

> Width of the gray lines that frame the plot elements.