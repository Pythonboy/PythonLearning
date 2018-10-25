# API reference



## Relational plots

| [`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot)([x, y, hue, size, style, data, row, …]) | Figure-level interface for drawing relational plots onto a FacetGrid. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`scatterplot`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot)([x, y, hue, style, size, data, …]) | Draw a scatter plot with possibility of several semantic groupings. |
| [`lineplot`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot)([x, y, hue, size, style, data, …]) | Draw a line plot with possibility of several semantic groupings. |



## Categorical plots

| [`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot)([x, y, hue, data, row, col, …]) | Figure-level interface for drawing categorical plots onto a FacetGrid. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`stripplot`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot)([x, y, hue, data, order, …]) | Draw a scatterplot where one variable is categorical.        |
| [`swarmplot`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot)([x, y, hue, data, order, …]) | Draw a categorical scatterplot with non-overlapping points.  |
| [`boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot)([x, y, hue, data, order, hue_order, …]) | Draw a box plot to show distributions with respect to categories. |
| [`violinplot`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot)([x, y, hue, data, order, …]) | Draw a combination of boxplot and kernel density estimate.   |
| [`boxenplot`](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot)([x, y, hue, data, order, …]) | Draw an enhanced box plot for larger datasets.               |
| [`pointplot`](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot)([x, y, hue, data, order, …]) | Show point estimates and confidence intervals using scatter plot glyphs. |
| [`barplot`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot)([x, y, hue, data, order, hue_order, …]) | Show point estimates and confidence intervals as rectangular bars. |
| [`countplot`](https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot)([x, y, hue, data, order, …]) | Show the counts of observations in each categorical bin using bars. |



## Distribution plots

| [`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot)(x, y[, data, kind, stat_func, …]) | Draw a plot of two variables with bivariate and univariate graphs. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`pairplot`](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot)(data[, hue, hue_order, palette, …]) | Plot pairwise relationships in a dataset.                    |
| [`distplot`](https://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot)(a[, bins, hist, kde, rug, fit, …]) | Flexibly plot a univariate distribution of observations.     |
| [`kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot)(data[, data2, shade, vertical, …]) | Fit and plot a univariate or bivariate kernel density estimate. |
| [`rugplot`](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot)(a[, height, axis, ax]) | Plot datapoints in an array as sticks on an axis.            |



## Regression plots

| [`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot)(x, y, data[, hue, col, row, palette, …]) | Plot data and regression model fits across a FacetGrid. |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [`regplot`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot)(x, y[, data, x_estimator, x_bins, …]) | Plot data and a linear regression model fit.            |
| [`residplot`](https://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot)(x, y[, data, lowess, x_partial, …]) | Plot the residuals of a linear regression.              |



## Matrix plots

| [`heatmap`](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap)(data[, vmin, vmax, cmap, center, …]) | Plot rectangular data as a color-encoded matrix.             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`clustermap`](https://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap)(data[, pivot_kws, method, …]) | Plot a matrix dataset as a hierarchically-clustered heatmap. |



## Multi-plot grids

### Facet grids

| [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid)(data[, row, col, hue, col_wrap, …]) | Multi-plot grid for plotting conditional relationships.      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`FacetGrid.map`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map)(func, *args, **kwargs) | Apply a plotting function to each facet’s subset of the data. |
| [`FacetGrid.map_dataframe`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html#seaborn.FacetGrid.map_dataframe)(func, *args, **kwargs) | Like `.map` but passes args as strings and inserts data in kwargs. |

### Pair grids

| [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid)(data[, hue, hue_order, palette, …]) | Subplot grid for plotting pairwise relationships in a dataset. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`PairGrid.map`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map.html#seaborn.PairGrid.map)(func, **kwargs) | Plot with the same function in every subplot.                |
| [`PairGrid.map_diag`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_diag.html#seaborn.PairGrid.map_diag)(func, **kwargs) | Plot with a univariate function on each diagonal subplot.    |
| [`PairGrid.map_offdiag`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_offdiag.html#seaborn.PairGrid.map_offdiag)(func, **kwargs) | Plot with a bivariate function on the off-diagonal subplots. |
| [`PairGrid.map_lower`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_lower.html#seaborn.PairGrid.map_lower)(func, **kwargs) | Plot with a bivariate function on the lower diagonal subplots. |
| [`PairGrid.map_upper`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_upper.html#seaborn.PairGrid.map_upper)(func, **kwargs) | Plot with a bivariate function on the upper diagonal subplots. |

### Joint grids

| [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid)(x, y[, data, height, ratio, …]) | Grid for drawing a bivariate plot with marginal univariate plots. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`JointGrid.plot`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot.html#seaborn.JointGrid.plot)(joint_func, marginal_func[, …]) | Shortcut to draw the full plot.                              |
| [`JointGrid.plot_joint`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_joint.html#seaborn.JointGrid.plot_joint)(func, **kwargs) | Draw a bivariate plot of x and y.                            |
| [`JointGrid.plot_marginals`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_marginals.html#seaborn.JointGrid.plot_marginals)(func, **kwargs) | Draw univariate plots for x and y separately.                |



## Style control

| [`set`](https://seaborn.pydata.org/generated/seaborn.set.html#seaborn.set)([context, style, palette, font, …]) | Set aesthetic parameters in one step.                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`axes_style`](https://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style)([style, rc]) | Return a parameter dict for the aesthetic style of the plots. |
| [`set_style`](https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style)([style, rc]) | Set the aesthetic style of the plots.                        |
| [`plotting_context`](https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context)([context, font_scale, rc]) | Return a parameter dict to scale elements of the figure.     |
| [`set_context`](https://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context)([context, font_scale, rc]) | Set the plotting context parameters.                         |
| [`set_color_codes`](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html#seaborn.set_color_codes)([palette]) | Change how matplotlib color shorthands are interpreted.      |
| [`reset_defaults`](https://seaborn.pydata.org/generated/seaborn.reset_defaults.html#seaborn.reset_defaults)() | Restore all RC params to default settings.                   |
| [`reset_orig`](https://seaborn.pydata.org/generated/seaborn.reset_orig.html#seaborn.reset_orig)() | Restore all RC params to original settings (respects custom rc). |



## Color palettes

| [`set_palette`](https://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette)(palette[, n_colors, desat, …]) | Set the matplotlib color cycle using a seaborn palette.      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`color_palette`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette)([palette, n_colors, desat]) | Return a list of colors defining a color palette.            |
| [`husl_palette`](https://seaborn.pydata.org/generated/seaborn.husl_palette.html#seaborn.husl_palette)([n_colors, h, s, l]) | Get a set of evenly spaced colors in HUSL hue space.         |
| [`hls_palette`](https://seaborn.pydata.org/generated/seaborn.hls_palette.html#seaborn.hls_palette)([n_colors, h, l, s]) | Get a set of evenly spaced colors in HLS hue space.          |
| [`cubehelix_palette`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette)([n_colors, start, rot, …]) | Make a sequential palette from the cubehelix system.         |
| [`dark_palette`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette)(color[, n_colors, reverse, …]) | Make a sequential palette that blends from dark to `color`.  |
| [`light_palette`](https://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette)(color[, n_colors, reverse, …]) | Make a sequential palette that blends from light to `color`. |
| [`diverging_palette`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette)(h_neg, h_pos[, s, l, sep, …]) | Make a diverging palette between two HUSL colors.            |
| [`blend_palette`](https://seaborn.pydata.org/generated/seaborn.blend_palette.html#seaborn.blend_palette)(colors[, n_colors, as_cmap, input]) | Make a palette that blends between a list of colors.         |
| [`xkcd_palette`](https://seaborn.pydata.org/generated/seaborn.xkcd_palette.html#seaborn.xkcd_palette)(colors) | Make a palette with color names from the xkcd color survey.  |
| [`crayon_palette`](https://seaborn.pydata.org/generated/seaborn.crayon_palette.html#seaborn.crayon_palette)(colors) | Make a palette with color names from Crayola crayons.        |
| [`mpl_palette`](https://seaborn.pydata.org/generated/seaborn.mpl_palette.html#seaborn.mpl_palette)(name[, n_colors]) | Return discrete colors from a matplotlib palette.            |

## Palette widgets

| [`choose_colorbrewer_palette`](https://seaborn.pydata.org/generated/seaborn.choose_colorbrewer_palette.html#seaborn.choose_colorbrewer_palette)(data_type[, as_cmap]) | Select a palette from the ColorBrewer set.                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`choose_cubehelix_palette`](https://seaborn.pydata.org/generated/seaborn.choose_cubehelix_palette.html#seaborn.choose_cubehelix_palette)([as_cmap]) | Launch an interactive widget to create a sequential cubehelix palette. |
| [`choose_light_palette`](https://seaborn.pydata.org/generated/seaborn.choose_light_palette.html#seaborn.choose_light_palette)([input, as_cmap]) | Launch an interactive widget to create a light sequential palette. |
| [`choose_dark_palette`](https://seaborn.pydata.org/generated/seaborn.choose_dark_palette.html#seaborn.choose_dark_palette)([input, as_cmap]) | Launch an interactive widget to create a dark sequential palette. |
| [`choose_diverging_palette`](https://seaborn.pydata.org/generated/seaborn.choose_diverging_palette.html#seaborn.choose_diverging_palette)([as_cmap]) | Launch an interactive widget to choose a diverging color palette. |

## Utility functions

| [`load_dataset`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset)(name[, cache, data_home]) | Load a dataset from the online repository (requires internet). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`despine`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine)([fig, ax, top, right, left, bottom, …]) | Remove the top and right spines from plot(s).                |
| [`desaturate`](https://seaborn.pydata.org/generated/seaborn.desaturate.html#seaborn.desaturate)(color, prop) | Decrease the saturation channel of a color by some percent.  |
| [`saturate`](https://seaborn.pydata.org/generated/seaborn.saturate.html#seaborn.saturate)(color) | Return a fully saturated color with the same hue.            |
| [`set_hls_values`](https://seaborn.pydata.org/generated/seaborn.set_hls_values.html#seaborn.set_hls_values)(color[, h, l, s]) | Independently manipulate the h, l, or s channels of a color. |