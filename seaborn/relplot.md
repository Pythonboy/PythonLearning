# seaborn.relplot

```python
seaborn.relplot(x=None, y=None, hue=None, size=None, style=None, data=None, row=None, col=None, col_wrap=None, row_order=None, col_order=None, palette=None, hue_order=None, hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=None, dashes=None, style_order=None, legend='brief', kind='scatter', height=5, aspect=1, facet_kws=None, **kwargs)
```



# Parameters

- **X , y** : names of variables in `data`

> Input data variables; must be numeric.

- **hue** :  name in `data`, optional

> Grouping variable that will produce elements with different colors. Can be either categorical or numeric, although color mapping will behave differently in latter case.

- **size** :  name in `data`, optional

> Grouping variable that will produce elements with different sizes. Can be either categorical or numeric, although size mapping will behave differently in latter case.

- **style** : name in `data`, optional

> Grouping variable that will produce elements with different styles. Can have a numeric dtype but will always be treated as categorical.

- **data** : DataFrame

> Tidy (“long-form”) dataframe where each column is a variable and each row is an observation.

- **row, col** : names of variables in `data`, optional

> Categorical variables that will determine the faceting of the grid.

- **col_wrap** : int, optional

> “Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a `row` facet.

- **palette** : palette name, list, or dict, optional

> Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette), or a dictionary mapping hue levels to matplotlib colors.

- **sizes** : list, dict, or tuple, optional

>  An object that determines how sizes are chosen when `size` is used.

- **legend** : “brief”, “full”, or False, optional

> How to draw the legend. If “brief”, numeric `hue` and `size` variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the legend. If `False`, no legend data is added and no legend is drawn.

- **height** : scalar, optional

> Height (in inches) of each facet. See also: `aspect`.

- **aspect** : scalar, optional

> Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.





















