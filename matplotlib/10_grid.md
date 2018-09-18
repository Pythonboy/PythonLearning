# 网格   

## 重要参数   
- linestyle : 线型
- linewidth : 线宽
- color ： 颜色

## Example   
```
x = np.linspace(0,10,100);
plt.figure()
plt.subplot(111)
plt.plot(x,x**2)
plt.grid(True)  # 打开网格
plt.grid(linewidth= '2', color = 'grey')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,np.sqrt(x))
ax.grid(linewidth = 0.5,color = 'green',linestyle = "-.")
plt.show()
```
