# Pandas统计函数

## pct_change()函数
**系列，DatFrames和Panel都有pct_change()函数。此函数将每个元素与其前一个元素进行比较，并计算变化百分比**
```
import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print (s.pct_change())
df = pd.DataFrame(np.random.randn(5, 2))
print (df.pct_change())
```
```
0        NaN
1   1.000000
2   0.500000
3   0.333333
4   0.250000
5  -0.200000
dtype: float64

            0          1
0         NaN        NaN
1  -15.151902   0.174730
2  -0.746374   -1.449088
3  -3.582229   -3.165836
4   15.601150  -1.860434
```
*默认情况下，pct_change()对列进行操作; 如果想应用到行上，那么可使用axis = 1参数*

## cov(协方差）
**协方差适用于系列数据。Series对象有一个方法cov用来计算序列对象之间的协方差。NA将被自动排除**

**Series**
```
import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print (s1.cov(s2))
```
```
0.0667296739178
```

**DataFrame**
```
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print (frame['a'].cov(frame['b']))
print (frame.cov())
```
```
-0.406796939839
          a         b         c         d         e
a  0.784886 -0.406797  0.181312  0.513549 -0.597385
b -0.406797  0.987106 -0.662898 -0.492781  0.388693
c  0.181312 -0.662898  1.450012  0.484724 -0.476961
d  0.513549 -0.492781  0.484724  1.571194 -0.365274
e -0.597385  0.388693 -0.476961 -0.365274  0.785044
```

## 相关性
**相关性显示了任何两个数值(系列)之间的线性关系。有多种方法来计算pearson(默认)，spearman和kendall之间的相关性**
```
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print (frame['a'].corr(frame['b']))
print (frame.corr())
```
```
-0.613999376618
          a         b         c         d         e
a  1.000000 -0.613999 -0.040741 -0.227761 -0.192171
b -0.613999  1.000000  0.012303  0.273584  0.591826
c -0.040741  0.012303  1.000000 -0.391736 -0.470765
d -0.227761  0.273584 -0.391736  1.000000  0.364946
e -0.192171  0.591826 -0.470765  0.364946  1.000000
```

## 数据排名
**数据排名为元素数组中的每个元素生成排名。在关系的情况下，分配平均等级。**
```
import pandas as pd
import numpy as np
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))
s['d'] = s['b'] # so there's a tie
print (s.rank())
```
```
a    4.0
b    1.5
c    3.0
d    1.5
e    5.0
dtype: float64
```
Rank可选地使用一个默认为true的升序参数; 当错误时，数据被反向排序，也就是较大的值被分配较小的排序。
Rank支持不同的tie-breaking方法，用方法参数指定 :
- average - 并列组平均排序等级
- min - 组中最低的排序等级
- max - 组中最高的排序等级
- first - 按照它们出现在数组中的顺序分配队列





