# 箱形图

```
matplotlib.pyplot.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, bootstrap=None, usermedians=None, conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None, manage_xticks=True, autorange=False, zorder=None, hold=None, data=None)
```

## 重要参数   
- notch = If True, will produce a notched box plot. Otherwise, a rectangular boxplot is produced
- sym : 最上面以及最下面异常值的点型
- whis : 两边直线所占比例，determines the reach of the whiskers to the beyond the first and third quartiles.，default 1.5
- labels ： list
- width : Sets the width of each box either with a scalar or a sequence,箱的宽度
- meanline : If True (and showmeans is True), will try to render the mean as a line spanning the full width of the box according to meanprops.
- showmeans : bool, optional (False) Show the arithmetic means


**example**
```
data = np.random.normal(size = (1000,4),loc = 0,scale = 1);
labels = [ 'a','b','c','d'];
plt.boxplot(data,labels = labels,sym = 'o',whis = 1.5,notch = False,widths = 0.3,meanline = False,showcaps = False,showmeans = True);
plt.show()
```
