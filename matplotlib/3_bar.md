# 条形图

```
bar(x, height, *, align='center', **kwargs)
bar(x, height, width, *, align='center', **kwargs)
bar(x, height, width, bottom, *, align='center', **kwargs)
```

**重要参数**
- x : sequence of scalars
- height : The height(s) of the bars.
- width : The width(s) of the bars (default: 0.8).
- bottom : The y coordinate(s) of the bars bases (default: 0).
- align : {'center', 'edge'}, optional, default: 'center'
- color : The colors of the bar faces.
- edgecolor : The colors of the bar edges.
- linewidth : Width of the bar edge(s). If 0, don't draw edges
- tick_label : The tick labels of the bars. Default: None (Use default numeric labels.)
- orientation : {'vertical', 'horizontal'}


**竖直条形图**
```
y = [30,20,15,17,26]
x = np.arange(5);
plt.bar(left =x,height = y, color = 'red',width = 0.5)
```
**水平条形图**
```
y = [30,20,15,17,26]
x = np.arange(5);
plt.bar(bottom =x,width = y,left = 0, color = 'red',height = 0.5,orientation = "horizontal")
```
```
y = [30,20,15,17,26]
x = np.arange(5);
plt.barh(bottom =x,width = y,left = 0, color = 'red',height = 0.5,orientation = "horizontal")
```

**并列条形图**
```
y = [30,20,15,17,26]
z = [40,45,23,56,23]
x = np.arange(5);
plt.bar(left = x,height = y,width = 0.3,color = 'red');
plt.bar(left = x+0.3,height = z,width = 0.3,color = 'green')
plt.show()
```

**叠加条形图**
```
y = [30,20,15,17,26]
z = [40,45,23,56,23]
x = np.arange(5);
plt.bar(left = x,height = y,width = 0.3,color = 'red');
plt.bar(left = x,bottom = y,height = z,width = 0.3,color = 'green')
plt.show()
```
