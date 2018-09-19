# 注释    

## annotate
```
matplotlib.pyplot.annotate(text, xy, *args, **kwargs)
```

### 重要参数
- text : 要注释的内容
- xy : 指定要注释的（x，y）点
- xytext : 指定（x，y）以放置文本。 如果为None，则默认为xy。
- arrowsprops : dic
1. width : 点的箭头宽度
2. headwidth : 箭头底部宽度
3. facecolor : 箭头颜色
4. frac : 箭头底部占全部箭头长度的比例
5. headlength : 箭头底部的长度

### Example

```
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = x**2;
plt.figure()
plt.plot(x,y,'g-.')
plt.annotate("this is the bottom",xy = (0,3),xytext = (-2.5,30),arrowprops = dict(facecolor = "red", frac = 0.2,headwidth = 20,width = 10))
plt.show()

```
```
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.set_ylim(-2, 2)
plt.show()
```
## text
```
matplotlib.pyplot.text(x, y, s, fontdict=None, withdash=False, **kwargs)
```
### 重要参数
- x,y : 放置文本的位置
- s : 文本内容，str
- fontdice : dict,设置文本属性
- family : 字体 "serif" "sans-serif" "cursive" "fantasy" "monospace"
- color : 颜色
- style : "normal"  "italic"
- size ： 字体大小
- weight： 字体的粗细















