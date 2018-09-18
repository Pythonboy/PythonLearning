# 折线图    

```
matplotlib.pyplot.plot(*args, **kwargs)[source]
```

**example**
```
x = np.linspace(0,10,100);
y = np.cos(x)
plt.plot(x,y,marker = 'o', linestyle = 'dashed',color = "red",alpha = 0.5);
plt.show()
```

## 重要参数   
- linestyple : 线型
- marker : 点型
- color : 颜色
- markersize : 点的大小
- linewidth : 线的宽度
- alpha : 透明度

```
>>> plot(x, y, 'go--', linewidth=2, markersize=12)
>>> plot(x, y, color='green', marker='o', linestyle='dashed',
        linewidth=2, markersize=12)
```

**example**
```
plt.plot(x,y,"bo-.");
plt.show()
```
```
plt.plot(x,np.sqrt(x),'g-.',x,np.sin(x),'b-',x,np.cos(x),'r--',x,x*2,'c:')
plt.show()
```
**format string**
```
fmt = '[color][marker][line]'
```
### color     
|character	|color|
|:-:|:-:|
|'b'|	blue|
|'g'|	green|
|'r'|red|
|'c'|	cyan|
|'m'	|magenta|
|'y'	|yellow|
|'k'|	black|
|'w'	|white|

### linestyle   
|character	|description|
|:-:|:-:|
|'-'	|solid line style|
|'--'|	dashed line style|
|'-.'|	dash-dot line style|
|':'	|dotted line style|
