# 坐标轴

## 坐标轴范围调整
**方法一:直接使用plt.axis()给出x轴，y轴的坐标范围 [xmin,xmax,ymin,ymax]** 
```
x = np.linspace(0,10,100);
y1 = x**2;
plt.figure()
plt.plot(x,y1);
plt.axis([0,10,0,100])
plt.show()
```
**方法二：单独调整一个坐标轴 plt.xlim([xmin,xmax]),plt.ylim([ymin,ymax])**
```
x = np.linspace(0,10,100);
y1 = x**2;
plt.figure()
plt.plot(x,y1);
plt.xlim([0,5])
plt.ylim(ymax = 40)
plt.show()
```

## 坐标轴刻度调整
### OO调整
```
x = np.linspace(0,10,100);
y1 = x**2;
plt.figure()
plt.plot(x,y1);
ax = plt.gca()    #获得当前图形坐标轴
ax.locator_params(nbins = 10) #如果前面系数给出'x' 'y'则单独改变一轴
plt.show()
```

### 交互式调整
```
x = np.linspace(0,10,100);
y1 = x**2;
plt.figure()
plt.plot(x,y1);
plt.gca()    #获得当前图形坐标轴
plt.locator_params('x',nbins = 20)
plt.show()
```

## 添加新的坐标轴
### 交互式   
```
x = np.linspace(0,10,100);
y1 = x**2;
y2 = np.sqrt(x);
plt.figure()
plt.plot(x,y1)
plt.twinx()
plt.plot(x,y2,'r-.')
plt.show()
```

### 面向对象式
**双Y轴**
```
x = np.linspace(0,10,100);
y1 = x**2;
y2 = np.sqrt(x);
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y1)
ax.set_ylabel("Y!")
ax2 = ax.twinx()
ax2.set_ylabel("Y2")
ax2.plot(x,y2,'r-.')
ax.set_xlabel("X")
plt.show()
```
**双X轴**
```
x = np.linspace(0,10,100);
y1 = x**2;
y2 = np.sqrt(x);
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y1,x)
ax2 = ax.twiny()
ax2.plot(y2,x,'r-.')
plt.show()
```
