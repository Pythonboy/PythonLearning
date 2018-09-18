# 图例

## legend()   
**重要参数**
- loc:   

|Location String|Location Code|
|:-:|:-:|
|'best'|	0|
|upper right'|1|
|'upper left'|	2|
|'lower left'	|3|
|'lower right'|	4|
|'right'	|5|
|'center left'|	6|
|center right'	|7|
|'lower center'	|8|
|'upper center'|	9|
|'center'	|10|

- title : 图例的名称
- ncol : int,表示图例按几列拍
- fontsize : int or float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}，图例中的字体大小
- shadow : bool,表示是否需要阴影
- framealpha ： 控制图例中背景颜色的透明度
- facecolor ： 背景颜色
- edgecolor : 图例边缘颜色

## 互动式
```
x = np.linspace(0,10,100);
y1 = x**2;
y2 = np.sqrt(x);
plt.figure()
plt.plot(x,y1,label = "1")
plt.plot(x,y2,label = "2")
plt.legend()
plt.show()
```


```
x = np.linspace(0,10,100);
y1 = x**2;
y2 = x*2;
plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(["Normed","Riht"],loc =0,title = "haha",ncol = 1,fontsize = 10,shadow = True,facecolor = "green",framealpha = 0.3,edgecolor = "red")
plt.show()
```
## 面向对象式
```
x = np.linspace(0,10,100);
y1 = x**2;
y2 = np.sqrt(x);
fig = plt.figure();
ax = fig.add_subplot(211)
ax.plot(x,y1);
ax.legend("L")
ax2 = fig.add_subplot(212)
ax2.plot(x,y2,label = "G")
ax2.legend()
plt.show()
```








