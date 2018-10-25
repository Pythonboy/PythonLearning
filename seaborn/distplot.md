# seaborn.distplot

**Flexibly plot a univariate distribution of observations.**

```python
seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)
```

This function combines the matplotlib `hist` function (with automatic calculation of a good default bin size) with the seaborn [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot) and [`rugplot()`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot) functions. It can also fit `scipy.stats` distributions and plot the estimated PDF over the data.



# Parameters

- **a** : Series, 1d-array, or list.

> Observed data. If this is a Series object with a `name` attribute, the name will be used to label the data axis.

- **bins** : argument for matplotlib hist(), or None, optional

> Specification of hist bins, or None to use Freedman-Diaconis rule.

- **hist** : bool, optional

> Whether to plot a (normed) histogram.

- **kde** : bool, optional

> Whether to plot a gaussian kernel density estimate.

- **rug** : bool, optional

> Whether to draw a rugplot on the support axis.

- **color** : matplotlib color, optional

> Color to plot everything but the fitted curve in.

- **vertical** : bool, optional

> If True, observed values are on y-axis.

- **axlabel** : string, False, or None, optional

> Name for the support axis label. If None, will try to get it from a.namel if False, do not set a label.

- **label** : string, optional

> Legend label for the relevent component of the plot































