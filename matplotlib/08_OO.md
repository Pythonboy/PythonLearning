# Matplotlib面向对象
|方式|简介|优劣势|
|:-:|:-:|:-:|
|pyplot|经典高层封装|简单易用，交互使用方便，可以根据命令实时作图，但底层定制能力不足|
|pylab|将matlab与numpy合并的模块，模拟Matlab的编程环境|完全封装，环境更接近Matlab|
|OO|Matplotlib的精髓，更基础和底层的方法|定制能力强|

## 子图
**fig = plt.figure()**
- 生成一个Figure实例
- 可以添加axes实例

**ax = fig.add_subplot(111)**
- 返回axes实例
- 参数1 ： 子图总行数
- 参数2 ： 子图总列数
- 参数3 ： 子图位置
- 这是在Figure上添加axes的常用方法


**面向对象式**
```
x = np.linspace(0,10,100)
fig = plt.figure()
ax = fig.add_subplot(221)
ax.plot(x,x);
ax2 = fig.add_subplot(222)
ax2.plot(x,x**2)
ax3 = fig.add_subplot(223)
ax3.plot(x,np.sqrt(x))
ax4 = fig.add_subplot(224)
ax4.plot(x,np.sin(x));
plt.show()
```

**交互式**
```
x = np.linspace(0,10,100)
plt.figure()
plt.subplot(221)
plt.plot(x,x)
plt.subplot(222)
plt.plot(x,x**2)
plt.subplot(223)
plt.plot(x,np.sqrt(x))
plt.subplot(224)
plt.plot(x,np.sin(x))
plt.show()
```
