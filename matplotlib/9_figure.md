# 多图Figure

**同时产生两张图**
*注意：这里的图是指画布，与一张画布中多张图是两种不同的概念*
```
x = np.linspace(0,10,100);
plt.figure()      #交互式
plt.subplot(111)
plt.plot(x,x**2)
fig = plt.figure()
ax = fig.add_subplot(111)   ##OO
ax.plot(x,np.sqrt(x))
plt.show()
```
