# seaborn.set

```
seaborn.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None
```

Set aesthetic parameters in one step.

Each set of parameters can be set directly or temporarily, see the referenced functions below for more information.



# Parameters

- **context** : string or dict

> Plotting context parameters, see [`plotting_context()`](https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context)

- **style** : string or dict

> Axes style parameters, see [`axes_style()`](https://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style)

- **palette** : string or sequence

> Color palette, see [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette)

- **font_scale** : float, optional

> Separate scaling factor to independently scale the size of the font elements.

- **color_codes** : bool

> If `True` and `palette` is a seaborn palette, remap the shorthand color codes (e.g. “b”, “g”, “r”, etc.) to the colors from this palette.