# 散点图   
```
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)
```

## 常用参数    
- s : 大小
- c : 颜色
- marker : 点型
- alpha : 透明度

**example**
```
import numpy as np
import matplotlib.pyplot as plt
N = 1000 ; 
x = np.random.randn(N);
y = np.random.randn(N)*0.5 - x;
plt.scatter(x,y,c ='red',alpha = 0.5,s = 10,marker = '<');
plt.show()
```

## marker   
|marker|	description|
|:-:|:-:|
|"."|	point|
|","	|pixel|
|"o"|	circle|
|"v"|	triangle_down|
|"^"	|triangle_up|
|"<"	|triangle_left|
|">"|	triangle_right|
|"1"	|tri_down|
|"2"	|tri_up|
|"3"|	tri_left|
|"4"|	tri_right|
|"8"	|octagon|
|"s"|	square|
|"p"|	pentagon|
|"P"	|plus (filled)|
|"*"	|star|
|"h"|	hexagon1|
|"H"|	hexagon2|
|"+"|	plus|
|"x"|	x|
|"X"|	x (filled)|
|"D"|	diamond|
|"d"|	thin_diamond|
|"|"|	vline|
|"_"	|hline|
