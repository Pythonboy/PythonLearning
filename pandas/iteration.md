# Pandas迭代  
**Pandas**对象之间的基本迭代的行为取决于类型。当迭代一个系列时，它被视为数组式，基本迭代产生这些值。其他数据结构，
如：DataFrame和Panel，遵循类似惯例迭代对象的键。  
简而言之，基本迭代(对于i在对象中)产生：
1. **Series** ： 值
2. **DataFrame** ： 列标签
3. **Panel** ： 项目标签  

## 迭代DataFrame  
迭代DataFrame提供列名
```
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

for col in df:
   print (col)
```
```
输出结果：
A
C
D
x
y
```

要遍历数据帧(DataFrame)中的行，可以使用以下函数
- **iteritems()** : 迭代(key，value)对 
- **iterrows()** : 将行迭代为(索引，系列)对
- **itertuples()** : 以namedtuples的形式迭代行

### iteritems()示例
**将每个列作为键，将值与值作为键和列值迭代为Series对象。**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print (key,value)
```
```
col1 0    0.802390
1    0.324060
2    0.256811
3    0.839186
Name: col1, dtype: float64

col2 0    1.624313
1   -1.033582
2    1.796663
3    1.856277
Name: col2, dtype: float64

col3 0   -0.022142
1   -0.230820
2    1.160691
3   -0.830279
Name: col3, dtype: float64
```

### iterrows()示例  
** iterrows()返回迭代器，产生每个索引值以及包含每行数据的序列 **
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print (row_index,row)
```
```
0  col1    1.529759
   col2    0.762811
   col3   -0.634691
Name: 0, dtype: float64

1  col1   -0.944087
   col2    1.420919
   col3   -0.507895
Name: 1, dtype: float64

2  col1   -0.077287
   col2   -0.858556
   col3   -0.663385
Name: 2, dtype: float64
3  col1    -1.638578
   col2     0.059866
   col3     0.493482
Name: 3, dtype: float64
```
*注意 - 由于iterrows()遍历行，因此不会跨该行保留数据类型。0,1,2是行索引，col1，col2，col3是列索引。*   

### itertuples()示例
**itertuples()方法将为DataFrame中的每一行返回一个产生一个命名元组的迭代器。元组的第一个元素将是行的相应索引值，而剩余的值是行值。**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print (row)
```
```
Pandas(Index=0, col1=1.5297586201375899, col2=0.76281127433814944, col3=-
0.6346908238310438)

Pandas(Index=1, col1=-0.94408735763808649, col2=1.4209186418359423, col3=-
0.50789517967096232)

Pandas(Index=2, col1=-0.07728664756791935, col2=-0.85855574139699076, col3=-
0.6633852507207626)

Pandas(Index=3, col1=0.65734942534106289, col2=-0.95057710432604969,
col3=0.80344487462316527)
```












