# seaborn.set_context

```python
seaborn.set_context(context=None, font_scale=1, rc=None)
```

Set the plotting context parameters.

This affects things like the size of the labels, lines, and other elements of the plot, but not the overall style. The base context is “notebook”, and the other contexts are “paper”, “talk”, and “poster”, which are version of the notebook parameters scaled by .8, 1.3, and 1.6, respectively.



# Parameters

- **context** : dict, None, or one of {paper, notebook, talk, poster}

> A dictionary of parameters or the name of a preconfigured set.

- **font_scale** : float, optional

> Separate scaling factor to independently scale the size of the font elements.

- **rc** : dict, optional

> Parameter mappings to override the values in the preset seaborn context dictionaries. This only updates parameters that are considered part of the context definition.



# Example

```python
set_context("paper")
```

```python
set_context("talk", font_scale=1.4)
```

```python
set_context("talk", rc={"lines.linewidth": 2})
```

