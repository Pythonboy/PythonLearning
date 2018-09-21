# 简单图形绘制
**根据坐标点绘制**
```
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([3,5,7,6,2,6,10,15])
plt.plot(x,y,'r')# 折线 1 x 2 y 3 color
plt.plot(x,y,'g',lw=10)# 4 line w
# 折线 饼状 柱状
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([13,25,17,36,21,16,10,15])
plt.bar(x,y,0.2,alpha=1,color='b')# 5 color 4 透明度 3 0.9
plt.show()
```

**根据函数图像绘制**
```
# -*- coding: utf-8 -*-
"""
简单图形绘制

"""
import matplotlib.pyplot as plt
import numpy as np

#从-1-----1之间等间隔采66个数.也就是说所画出来的图形是66个点连接得来的
#注意：如果点数过小的话会导致画出来二次函数图像不平滑
x = np.linspace(-1, 1,66)
# 绘制y=2x+1函数的图像
y = 2 * x + 1
plt.plot(x, y)
plt.show()

# 绘制x^2函数的图像
y = x**2
plt.plot(x, y)
plt.show()
```

# figure的简单使用
```
# -*- coding: utf-8 -*-
"""
figure的使用
"""
import matplotlib.pyplot as plt
import numpy as np
# 
x = np.linspace(-1, 1, 50)

# figure 1
y1 = 2 * x + 1
plt.figure()
plt.plot(x, y1)

# figure 2
y2 = x**2
plt.figure()
plt.plot(x, y2)

# figure 3，指定figure的编号并指定figure的大小, 指定线的颜色, 宽度和类型
#一个坐标轴上画了两个图形
y2 = x**2
plt.figure(num = 5, figsize = (4, 4))
plt.plot(x, y1)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')
plt.show()
```

# 设置坐标轴
```
# -*- coding: utf-8 -*-
"""
设置坐标轴
"""
import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')

# 设置坐标轴的取值范围
plt.xlim((-1, 1))
plt.ylim((0, 3))

# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'这是x轴',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'这是y轴',fontproperties='SimHei',fontsize=14)

# 设置x坐标轴刻度, 之前为0.25, 修改后为0.5
#也就是在坐标轴上取5个点，x轴的范围为-1到1所以取5个点之后刻度就变为0.5了
plt.xticks(np.linspace(-1, 1, 5))
plt.show()
```

**在上面的代码基础之上加入下面代码，可以使右边框和上边框消失，同时使坐标原点设置在（0，0）位置上**
```
ax = plt.gca();
ax.spines['right'].set_color("none");
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('data',0));
ax.spines['left'].set_position(('data',0));
```

```
#设置坐标轴label的大小，背景色等信息
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'green', edgecolor = 'None', alpha = 0.7))
```

# 移动spines
spines包括图片上下左右4条边界和它们的下标，就是正方形的4条边。它们可以被挪到任意的位置，现在，它们还在边界上。我们要把它们移到中间。首先，将上边界和右边界的颜色设置为none，就隐藏了。然后我们将下边界和左边界移动到数据空间的0处。 
```
# plt.gca()获取当前ax
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
# set_position中的参数元组的第二个值可取-1，0，1分别代表相对‘data’的不同的位置
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
```

# 设置坐标轴下标名
```
# r''是为了转义里面的转义字符\
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
```

# 添加注解和绘制点以及在图形上绘制线或点
```
# -*- coding: utf-8 -*-
"""
添加注解和绘制点以及在图形上绘制线或点
"""

import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure()
plt.plot(x, y)

# 将上、右边框去掉
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x轴的位置及数据在坐标轴上的位置
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# 设置y轴的位置及数据在坐标轴上的位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 定义(x0, y0)点
x0 = 1
y0 = 2 * x0 + 1

# 绘制(x0, y0)点
plt.scatter(x0, y0, s = 50, color = 'blue')
# 绘制虚线
plt.plot([x0, x0], [y0, 0], 'k--', lw = 2.5)
# 绘制注解一
plt.annotate(r'$2 * x + 1 = %s$' % y0, xy = (x0, y0), xycoords = 'data', xytext = (+30, -30), \
             textcoords = 'offset points', fontsize = 16, arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = .2'))

# 绘制注解二
plt.text(-3, 3, r'$Test\ text. \mu \sigma_i, \alpha_i$', fontdict = {'size': 16, 'color': 'red'})
plt.show()
```

# 散点图  
```
# -*- coding: utf-8 -*-
"""
绘制散点图
"""
import numpy as np
import matplotlib.pyplot as plt

# 数据个数
n = 1024
# 均值为0, 方差为1的随机数
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

# 计算颜色值
color = np.arctan2(y, x)
# 绘制散点图
plt.scatter(x, y, s = 75, c = color, alpha = 0.5)
# 设置坐标轴范围
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

# 不显示坐标轴的值
plt.xticks(())
plt.yticks(())

plt.show()
```

# 柱状图  
```
# -*- coding: utf-8 -*-
"""
绘制柱状图
"""

import matplotlib.pyplot as plt
import numpy as np

# 数据数目
n = 10
x = np.arange(n)
# 生成数据, 均匀分布(0.5, 1.0)之间
y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

# 绘制柱状图, 向上
plt.bar(x, y1, facecolor = 'blue', edgecolor = 'white')
# 绘制柱状图, 向下
plt.bar(x, -y2, facecolor = 'green', edgecolor = 'white')


temp = zip(x, y2)
# 在柱状图上显示具体数值, ha水平对齐, va垂直对齐
for x, y in zip(x, y1):
    plt.text(x + 0.05, y + 0.1, '%.2f' % y, ha = 'center', va = 'bottom')

for x, y in temp:
    plt.text(x + 0.05, -y - 0.1, '%.2f' % y, ha = 'center', va = 'bottom')

# 设置坐标轴范围
plt.xlim(-1, n)
plt.ylim(-1.5, 1.5)
# 去除坐标轴
plt.xticks(())
plt.yticks(())
plt.show()
```

# 绘制登高线图   
```
# -*- coding: utf-8 -*-
"""
绘制登高线图
"""
import matplotlib.pyplot as plt
import numpy as np

# 定义等高线高度函数
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(- x ** 2 - y ** 2)

# 数据数目
n = 256
# 定义x, y
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# 生成网格数据
X, Y = np.meshgrid(x, y)

# 填充等高线的颜色, 8是等高线分为几部分
plt.contourf(X, Y, f(X, Y), 8, alpha = 0.75, cmap = plt.cm.hot)
# 绘制等高线
C = plt.contour(X, Y, f(X, Y), 8, colors = 'black', linewidth = 0.5)
# 绘制等高线数据
plt.clabel(C, inline = True, fontsize = 10)

# 去除坐标轴
plt.xticks(())
plt.yticks(())
plt.show()
```

# 绘制3D图像
```
# -*- coding: utf-8 -*-
"""
绘制3d图形
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# 定义figure
fig = plt.figure()
# 将figure变为3d
ax = Axes3D(fig)

# 数据数目
n = 256
# 定义x, y
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

# 生成网格数据
X, Y = np.meshgrid(x, y)

# 计算每个点对的长度
R = np.sqrt(X ** 2 + Y ** 2)
# 计算Z轴的高度
Z = np.sin(R)

# 绘制3D曲面
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))
# 绘制从3D曲面到底部的投影
ax.contour(X, Y, Z, zdim = 'z', offset = -2, cmap = 'rainbow')

# 设置z轴的维度
ax.set_zlim(-2, 2)

plt.show()
```

# 多图
## subplot绘制多图
```
# -*- coding: utf-8 -*-
"""
subplot绘制多图 
"""

import matplotlib.pyplot as plt

plt.figure()

# 绘制第一个图
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])
# 绘制第二个图
plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 1])
# 绘制第三个图
plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 1])
# 绘制第四个图
plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 1])
plt.show()
```
```
# -*- coding: utf-8 -*-
"""
subplot绘制多图 
"""

import matplotlib.pyplot as plt

plt.figure()

# 绘制第一个图
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])
# 绘制第二个图
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])
# 绘制第三个图
plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 1])
# 绘制第四个图
plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 1])
plt.show()
```

## subplot2grid && gridspec
```
# -*- coding: utf-8 -*-
"""
figure绘制多图 
"""
# -*- coding: utf-8 -*-
"""
figure绘制多图 
"""
import matplotlib.pyplot as plt

# 定义figure
plt.figure()
# figure分成3行3列, 取得第一个子图的句柄, 第一个子图跨度为1行3列, 起点是表格(0, 0)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan = 3, rowspan = 1)
ax1.plot([0, 1], [0, 1])
ax1.set_title('Test')

# figure分成3行3列, 取得第二个子图的句柄, 第二个子图跨度为1行3列, 起点是表格(1, 0)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan = 2, rowspan = 1)
ax2.plot([0, 1], [0, 1])

# figure分成3行3列, 取得第三个子图的句柄, 第三个子图跨度为1行1列, 起点是表格(1, 2)
ax3 = plt.subplot2grid((3, 3), (1, 2), colspan = 1, rowspan = 1)
ax3.plot([0, 1], [0, 1])

# figure分成3行3列, 取得第四个子图的句柄, 第四个子图跨度为1行3列, 起点是表格(2, 0)
ax4 = plt.subplot2grid((3, 3), (2, 0), colspan = 3, rowspan = 1)
ax4.plot([0, 1], [0, 1])

plt.show()
```
```
# -*- coding: utf-8 -*-
"""
figure绘制多图 
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 定义figure
plt.figure()
# 分隔figure
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0:2])
ax3 = plt.subplot(gs[1, 2])
ax4 = plt.subplot(gs[2, :])

# 绘制图像
ax1.plot([0, 1], [0, 1])
ax1.set_title('Test')

ax2.plot([0, 1], [0, 1])

ax3.plot([0, 1], [0, 1])

ax4.plot([0, 1], [0, 1])

plt.show()
```

# 图的嵌套
```
# -*- coding: utf-8 -*-
"""
figure图的嵌套
"""

import matplotlib.pyplot as plt

# 定义figure
fig = plt.figure()

# 定义数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# figure的百分比, 从figure 10%的位置开始绘制, 宽高是figure的80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# 获得绘制的句柄
ax1 = fig.add_axes([left, bottom, width, height])
# 绘制点(x,y)
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('test')

# 嵌套方法一
# figure的百分比, 从figure 10%的位置开始绘制, 宽高是figure的80%
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
# 获得绘制的句柄
ax2 = fig.add_axes([left, bottom, width, height])
# 绘制点(x,y)
ax2.plot(x, y, 'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('part1')

# 嵌套方法二
plt.axes([bottom, left, width, height])
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('part2')

plt.show()
```

# 主次坐标轴
```
# -*- coding: utf-8 -*-
"""
主次坐标轴 
"""
import numpy as np
import matplotlib.pyplot as plt

# 定义数据
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x ** 2
y2 = -1 * y1

# 定义figure
fig, ax1 = plt.subplots()
# 得到ax1的对称轴ax2
ax2 = ax1.twinx()
# 绘制图像
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')

# 设置label
ax1.set_xlabel('X data')
ax1.set_xlabel('Y1', color = 'g')
ax2.set_xlabel('Y2', color = 'b')

plt.show()
```

# 共享坐标轴
```
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# sharex表示共享X轴，sharey表示共享y轴
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
# 显示点（1, 2）, （1, 2）
ax11.scatter([1, 2], [1, 2])

ax11.set_title('11')
ax12.set_title('11')
ax21.set_title('21')
ax22.set_title('22')

plt.tight_layout()
plt.show()
```

#Animation 动画
```
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots()

# 从[0, 2*np.pi]以0.01为间隔，形成一个列表
x = np.arange(0, 2*np.pi, 0.01)
# 这里只需要列表的第一个元素，所以就用逗号“,”加空白的形式省略了列表后面的元素
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/100))
    return line, 

def init():
    line.set_ydata(np.sin(x))
    # 这里由于仅仅需要列表的第一个参数，所以后面的就直接用空白省略了
    return line,  

ani = animation.FuncAnimation(fig=fig, 
                              func=animate,  # 动画函数
                              frames=100,   # 帧数
                              init_func=init,  # 初始化函数
                              interval=20,  # 20ms
                              blit=True)

plt.show()
```

# Matplotlib组件
## Figure
一个figure就是一个在GUI中名为“Figure#”的一个窗口，它的计数是从1开始的，跟普通的Python计数方式不同，而是MATLAB的计数风格。下面是几个定义figure外形的参数
|参数	|默认值	|描述|
|:-:|:-:|:-:|
|num	|1|	figure编号|
|figsize|	figure.figsize|	figure长和宽|
|dpi	|figure.dpi|	像素|
|facecolor	|figure.facecolor|	背景颜色|
|edgecolor	|figure.edgecolor|	边缘颜色|
|frameon	|True|	边框有无|

## subplot
subplot是用来布局plots的，需要指定（行、列、序号）
```
from pylab import *
import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(3, 3)

axes_1 = subplot(G[0, :])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

axes_2 = subplot(G[1,:-1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

axes_3 = subplot(G[1:, -1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

axes_4 = subplot(G[-1,0])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)

axes_5 = subplot(G[-1,-2])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)

#plt.savefig('../figures/gridspec.png', dpi=64)
show()
```

```
from pylab import *

subplot(2,2,1)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,1)',ha='center',va='center',size=20,alpha=.5)

subplot(2,2,2)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,2)',ha='center',va='center',size=20,alpha=.5)

subplot(2,2,3)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,3)',ha='center',va='center',size=20,alpha=.5)

subplot(2,2,4)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,4)',ha='center',va='center',size=20,alpha=.5)

# savefig('../figures/subplot-grid.png', dpi=64)
show()
```

## Axes
Axes和subplots很像，但它可以布局在figure的任意位置。所以如果我们想把一个小plot放在一个大plot里面，应该采用Axes。 
```
from pylab import *

axes([0.1,0.1,.8,.8])
xticks([]), yticks([])
text(0.6,0.6, 'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)

axes([0.2,0.2,.3,.3])
xticks([]), yticks([])
text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)

plt.savefig("../figures/axes.png",dpi=64)
show()
```

```
from pylab import *

axes([0.1,0.1,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.1,0.1,.8,.8])',ha='left',va='center',size=16,alpha=.5)

axes([0.2,0.2,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.2,0.2,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.3,0.3,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.3,0.3,.5,.5])',ha='left',va='center',size=16,alpha=.5)

axes([0.4,0.4,.5,.5])
xticks([]), yticks([])
text(0.1,0.1, 'axes([0.4,0.4,.5,.5])',ha='left',va='center',size=16,alpha=.5)

# plt.savefig("../figures/axes-2.png",dpi=64)
show()
```














