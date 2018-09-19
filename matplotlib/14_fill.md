# 区域填充
## fill()函数
```
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,6*np.pi);
y = np.sin(x);
z = np.sin(2*x);
plt.figure();
plt.fill(x,y,'r',alpha = 0.3);
plt.fill(x,z,'g',alpha = 0.3);
plt.show()
```


## fillbetween()函数
```
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,6*np.pi,1000);
y = np.sin(x);
z = np.sin(2*x);
fig = plt.figure();
ax = fig.add_subplot(111);
ax.plot(x,y,x,z)
ax.fill_between(x,y,z,where=y>z,facecolor = 'r',alpha = 0.3,interpolate = True);
ax.fill_between(x,y,z,where=z>y,facecolor = 'g',alpha = 0.3,interpolate = True);
plt.show()
```
