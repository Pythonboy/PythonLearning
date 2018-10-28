# seaborn.violinplot

```python
seaborn.violinplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, bw='scott', cut=2, scale='area', scale_hue=True, gridsize=100, width=0.8, inner='box', split=False, dodge=True, orient=None, linewidth=None, color=None, palette=None, saturation=0.75, ax=None, **kwargs)
```

**Draw a combination of boxplot and kernel density estimate.**

A violin plot plays a similar role as a box and whisker plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution.

This can be an effective and attractive way to show multiple distributions of data at once, but keep in mind that the estimation procedure is influenced by the sample size, and violins for relatively small samples might look misleadingly smooth.



# Parameters

- **x, y, hue** : names of variables in `data` or vector data, optional

> Inputs for plotting long-form data. See examples for interpretation.

- **data** : DataFrame, array, or list of arrays, optional

> Dataset for plotting. If `x` and `y` are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.

- **order, hue_order** : lists of strings, optional

> Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.

- **bw** : {‘scott’, ‘silverman’, float}, optional

> Either the name of a reference rule or the scale factor to use when computing the kernel bandwidth.

- **cut** : float, optional

> Distance, in units of bandwidth size, to extend the density past the extreme datapoints. 

- **scale** : {“area”, “count”, “width”}, optional

> The method used to scale the width of each violin. If `area`, each violin will have the same area. If `count`, the width of the violins will be scaled by the number of observations in that bin. If `width`, each violin will have the same width.

- **gridsize** : int, optional

> Number of points in the discrete grid used to compute the kernel density estimate.

- **width** : float, optional

> Width of a full element when not using hue nesting, or width of all the elements for one level of the major grouping variable.

- **inner** : {“box”, “quartile”, “point”, “stick”, None}, optional

> Representation of the datapoints in the violin interior. If `box`, draw a miniature boxplot. If `quartiles`, draw the quartiles of the distribution. If `point` or `stick`, show each underlying datapoint. Using `None` will draw unadorned violins.

- **dodge** : bool, optional

> When hue nesting is used, whether elements should be shifted along the categorical axis.

- **orient** : “v” | “h”, optional

> Orientation of the plot (vertical or horizontal).

- **linewidth** : float, optional

> Width of the gray lines that frame the plot elements.

- **color** : matplotlib color, optional

> Color for all of the elements, or seed for a gradient palette.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable.