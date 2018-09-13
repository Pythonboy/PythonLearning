# Pandas索引和选择数据
** Pandas现在支持三种类型的多轴索引 **   

|编号|索引|	描述|
|:-:|:-:|:-:|
|1|	.loc()|	基于标签|
|2|	.iloc()|	基于整数|
|3|	.ix()|	基于标签和整数|

## .loc()
loc()具有多种访问方式，如:
- 单个标量标签
- 标签列表
- 切片对象
- 一个布尔数组

** loc需要两个单/列表/范围运算符，用","分隔。第一个表示行，第二个表示列 **

**示例1**
```
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print (df.loc[:,'A'])
```
```
a    0.015860
b   -0.014135
c    0.446061
d    1.801269
e   -1.404779
f   -0.044016
g    0.996651
h    0.764672
Name: A, dtype: float64
```

**示例2** 
```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select all rows for multiple columns, say list[]
print (df.loc[:,['A','C']])
```
```
          A         C
a -0.529735 -1.067299
b -2.230089 -1.798575
c  0.685852  0.333387
d  1.061853  0.131853
e  0.990459  0.189966
f  0.057314 -0.370055
g  0.453960 -0.624419
h  0.666668 -0.433971
```

**示例3**
```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print (df.loc[['a','b','f','h'],['A','C']])
# Select all rows for multiple columns, say list[]
print (df.loc[:,['A','C']])
```
```
          A         C
a -1.959731  0.720956
b  1.318976  0.199987
f -1.117735 -0.181116
h -0.147029  0.027369
          A         C
a -1.959731  0.720956
b  1.318976  0.199987
c  0.839221 -1.611226
d  0.722810  1.649130
e -0.524845 -0.037824
f -1.117735 -0.181116
g -0.642907  0.443261
h -0.147029  0.027369
```

**示例4**
```
# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print (df.loc['a':'h'])
```
```
          A         B         C         D
a  1.556186  1.765712  1.060657  0.810279
b  1.377965 -0.183283 -0.224379  0.963105
c -0.530016  0.167183 -0.066459  0.074198
d -1.515189 -1.453529 -1.559400  1.072148
e -0.487399  0.436143 -1.045622 -0.029507
f  0.552548  0.410745  0.570222 -0.628133
g  0.865293 -0.638388  0.388827 -0.469282
h -0.690596  1.765139 -0.492070 -0.176074
```

**示例5**
```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# for getting values with a boolean array
print (df.loc['a']>0)
```
```
A    False
B     True
C    False
D     True
Name: a, dtype: bool
```

## iloc()
** Pandas提供了各种方法，以获得纯整数索引。像python和numpy一样，第一个位置是基于0的索引 **  

各种访问方式如下:
- 整数
- 整数列表
- 系列值

**示例1**
```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print (df.iloc[:4])
```
```
        A         B         C         D
0  0.277146  0.274234  0.860555 -1.312323
1 -1.064776  2.082030  0.695930  2.409340
2  0.033953 -1.155217  0.113045 -0.028330
3  0.241075 -2.156415  0.939586 -1.670171
```

**示例2**
```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print (df.iloc[:4])
print (df.iloc[1:5, 2:4])
```
```
         A         B         C         D
0  1.346210  0.251839  0.975964  0.319049
1  0.459074  0.038155  0.893615  0.659946
2 -1.097043  0.017080  0.869331 -1.443731
3  1.008033 -0.189436 -0.483688 -1.167312
          C         D
1  0.893615  0.659946
2  0.869331 -1.443731
3 -0.483688 -1.167312
4  1.566395 -1.292206
```

**示例3**
```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Slicing through list of values
print (df.iloc[[1, 3, 5], [1, 3]])
print (df.iloc[1:3, :])
print (df.iloc[:,1:3])
```
```
          B         D
1  0.081257  0.009109
3  1.037680 -1.467327
5  1.106721  0.320468
          A         B         C         D
1 -0.133711  0.081257 -0.031869  0.009109
2  0.895576 -0.513450 -0.048573  0.698965
          B         C
0  0.442735 -0.949859
1  0.081257 -0.031869
2 -0.513450 -0.048573
3  1.037680 -0.801157
4 -0.547456 -0.255016
5  1.106721  0.688142
6 -0.466452  0.219914
7  1.583112  0.982030
```


## ix()
**除了基于纯标签和整数之外，Pandas还提供了一种使用.ix()运算符进行选择和子集化对象的混合方法**

**示例1**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# Integer slicing
print (df.ix[:4])
```
```
          A         B         C         D
0 -1.449975 -0.002573  1.349962  0.539765
1 -1.249462 -0.800467  0.483950  0.187853
2  1.361273 -1.893519  0.307613 -0.119003
3 -0.103433 -1.058175 -0.587307 -0.114262
4 -0.612298  0.873136 -0.607457  1.047772

```

**示例2**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# Index slicing
print (df.ix[:,'A'])
```
```
0    1.539915
1    1.359477
2    0.239694
3    0.563254
4    2.123950
5    0.341554
6   -0.075717
7   -0.606742
Name: A, dtype: float64
```


## 使用符号
**使用多轴索引从Pandas对象获取值可使用以下符号 **  

|对象|	索引|	描述|
|:-:|:-:|:-:|
|Series|	s.loc[indexer]	|标量值|
|DataFrame|	df.loc[row_index,col_index]	|标量对象|
|Panel	|p.loc[item_index,major_index, minor_index]|	p.loc[item_index,major_index, minor_index]|

**现在来看看如何在DataFrame对象上执行每个操作。这里使用基本索引运算符[]**

**示例1**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df['A'])
```
```
0    0.028277
1   -1.037595
2   -0.563495
3   -1.196961
4   -0.805250
5   -0.911648
6   -0.355171
7   -0.232612
Name: A, dtype: float64
```

**示例2**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df[['A','B']])
```
```
          A         B
0 -0.767339 -0.729411
1 -0.563540 -0.639142
2  0.873589 -2.166382
3  0.900330  0.253875
4 -0.520105  0.064438
5 -1.452176 -0.440864
6 -0.291556 -0.861924
7 -1.464235  0.313168
```

**示例3**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df[2:2])
```
```
Empty DataFrame
Columns: [A, B, C, D]
Index: []
```


## 属性访问
**可以使用属性运算符.来选择列**
```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print (df.A)
```
```
0    0.104820
1   -1.206600
2    0.469083
3   -0.821226
4   -1.238865
5    1.083185
6   -0.827833
7   -0.199558
Name: A, dtype: float64
```


