# 直方图    

```
matplotlib.pyplot.hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, hold=None, data=None, **kwargs)[source]
```

## 重要参数
|参数|作用|
|:-:|:-:|
|bins|数据分为多少块|
|range|he lower and upper range of the bins,If not provided, range is (x.min(), x.max())|
|bottom|default:0,Location of the bottom baseline of each bin|
|histtype|{'bar', 'barstacked', 'step', 'stepfilled'}, optional|
|align|{'left', 'mid', 'right'}|
|orientation|{'horizontal', 'vertical'}|


**example**
```
mu = 100;
sigma = 20;
x = mu + sigma*np.random.randn(2000);
plt.hist(x,bins = 100,color = 'green',normed = False,edgecolor = 'k',histtype = 'step');
plt.show()
```

## hist2d
```
matplotlib.pyplot.hist2d(x, y, bins=10, range=None, normed=False, weights=None, cmin=None, cmax=None, hold=None, data=None, **kwargs)[source]
```
**重要参数**
- color : 颜色
- alpha ： 透明度
- bins : 分块数


