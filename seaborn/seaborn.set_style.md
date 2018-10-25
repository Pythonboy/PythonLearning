# seaborn.set_style

```
seaborn.set_style(style=None, rc=None)
```

Set the aesthetic style of the plots.

This affects things like the color of the axes, whether a grid is enabled by default, and other aesthetic elements.



# Parameters

- **style** : dict, None, or one of {darkgrid, whitegrid, dark, white, ticks}

> A dictionary of parameters or the name of a preconfigured set.

- **rc** : dict, optional

> Parameter mappings to override the values in the preset seaborn style dictionaries. This only updates parameters that are considered part of the style definition.



# Examples

```python
set_style("whitegrid")
```

```python
set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})
```

