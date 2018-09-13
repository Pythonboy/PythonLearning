# Pandas描述性统计
有很多方法用来集体计算DataFrame的描述性统计信息和其他相关操作。 其中大多数是sum()，mean()等聚合函数，但其中一些，如sumsum()，产生一个
相同大小的对象。 一般来说，这些方法采用轴参数，就像ndarray.{sum，std，...}，但轴可以通过名称或整数来指定：
数据帧(DataFrame) - “index”(axis=0，默认)，columns(axis=1)
下面创建一个数据帧(DataFrame)，并使用此对象进行演示本章中所有操作
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df
```
```
输出结果：
    Age  Name   Rating
0   25   Tom     4.23
1   26   James   3.24
2   25   Ricky   3.98
3   23   Vin     2.56
4   30   Steve   3.20
5   29   Minsu   4.60
6   23   Jack    3.80
7   34   Lee     3.78
8   40   David   2.98
9   30   Gasper  4.80
10  51   Betina  4.10
11  46   Andres  3.65
```

## sum()方法
**返回所请求轴的值的总和** 
* 默认情况下，轴为索引(axis=0)*
```
import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.sum()
```
```
输出结果：
Age                                                    382
Name     TomJamesRickyVinSteveMinsuJackLeeDavidGasperBe...
Rating                                               44.92
dtype: object
```

**axis = 1的情况**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.sum(1)
```
```
输出结果：
0    29.23
1    29.24
2    28.98
3    25.56
4    33.20
5    33.60
6    26.80
7    37.78
8    42.98
9    34.80
10   55.10
11   49.65
dtype: float64
```

## mean()
**返回平均值**
```
import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.mean()
```
```
输出结果：
Age       31.833333
Rating     3.743333
dtype: float64
```

## std()
**计算数字列的Bressel标准偏差**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.std()
```
```
输出结果：
Age       9.232682
Rating    0.661628
dtype: float64
```

---

# 重要函数

## 汇总

|编号|函数|描述|
|:-:|:-:|:-:|
|1|count()|非空观测数量|
|2|sum()|所有值之和|
|3|mean()|所有值的平均值|
|4|meadian()|所有值的中位数|
|5|mode()|值的模值|
|6|std()|值的标准偏差|
|7|min()|所有值中的最小值|
|8|max()|所有值中的最大值|
|9|abs()|绝对值|
|10|prod()|数组元素的乘积|
|11|cumsum()|累计总和|
|12|cumprod()|累计总积|

## 汇总数据

### describe()
**describe()函数是用来计算有关DataFrame列的统计信息的摘要**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.describe()
```
```
输出结果：
               Age         Rating
count    12.000000      12.000000
mean     31.833333       3.743333
std       9.232682       0.661628
min      23.000000       2.560000
25%      25.000000       3.230000
50%      29.500000       3.790000
75%      35.500000       4.132500
max      51.000000       4.800000
```
该函数给出了平均值，标准差和IQR值。 而且，函数排除字符列，并给出关于数字列的摘要。

**include**是用于传递关于什么列需要考虑用于总结的必要信息的参数。获取值列表; 默认情况下是”数字值”。
- **object** : 汇总字符串列
- **number** : 汇总数字列
- **all** : 将所有列汇总在一起(不应将其作为列表值传递)

```
import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print df.describe(include=['object'])
```
```
输出结果：
          Name
count       12
unique      12
top      Ricky
freq         1
```

```
import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print df. describe(include='all')
```
```
输出结果：
         Age          Name       Rating
count   12.000000        12    12.000000
unique        NaN        12          NaN
top           NaN     Ricky          NaN
freq          NaN         1          NaN
mean    31.833333       NaN     3.743333
std      9.232682       NaN     0.661628
min     23.000000       NaN     2.560000
25%     25.000000       NaN     3.230000
50%     29.500000       NaN     3.790000
75%     35.500000       NaN     4.132500
max     51.000000       NaN     4.800000
```







