# seaborn.jointplot

**Draw a plot of two variables with bivariate and univariate graphs**

```python
seaborn.jointplot(x, y, data=None, kind='scatter', stat_func=None, color=None, height=6, ratio=5, space=0.2, dropna=True, xlim=None, ylim=None, joint_kws=None, marginal_kws=None, annot_kws=None, **kwargs)
```



# Parameters

- **x , y** : strings or vectors

> Data or names of variables in `data`.

- **data** : DataFrame, optional

> DataFrame when `x` and `y` are variable names.

- **kind** : { “scatter” | “reg” | “resid” | “kde” | “hex” }, optional

> Kind of plot to draw.

- **color** : matplotlib color, optional

> Color used for the plot elements.

- **height** : numeric, optional

> Size of the figure (it will be square).

- **ratio** : numeric, optional

> Ratio of joint axes height to marginal axes height.

- **space** : numeric, optional

> Space between the joint and marginal axes

- **dropna** : bool, optional

> If True, remove observations that are missing from `x` and `y`.











































