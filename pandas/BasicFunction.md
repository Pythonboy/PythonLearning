# Series系列基本功能   
- axes : 返回行轴标签列表
- dtype ：返回对象的数据类型(dtype)
- empty ： 如果系列为空，则返回True
- ndim ： 返回底层数据的维数，默认定义：1
- size ： 返回基础数据中的元素数
- values ： 将系列作为ndarray返回
- head() : 返回前n行
- tail() : 返回最后n行

```
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print s
```

**输出结果**
```
0   0.967853
1  -0.148368
2  -1.395906
3  -1.758394
dtype: float64
```  

## axes示例  
*返回系列的标签列表*
```
import pandas as pd
import numpy as np
#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print ("The axes are:")
print s.axes
```
```
输出结果：
The axes are:
[RangeIndex(start=0, stop=4, step=1)]
```

## empty示例   
```
import pandas as pd
import numpy as np
#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print ("Is the Object empty?")
print s.empty
```
```
输出结果：
Is the Object empty?
False
```

## ndim示例
```
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print s

print ("The dimensions of the object:")
print s.ndim
```
```
输出结果
0   0.175898
1   0.166197
2  -0.609712
3  -1.377000
dtype: float64

The dimensions of the object:
1
```

## size示例
```
返回系列的大小（长度）
import pandas as pd
import numpy as np
#Create a series with 4 random numbers
s = pd.Series(np.random.randn(2))
print s
print ("The size of the object:")
print s.size
```
```
输出结果：
0   3.078058
1  -1.207803
dtype: float64

The size of the object:
2
```

## values示例
```
以数组形式返回系列中的实际数据值。
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print s

print ("The actual data series is:")
print s.values
```
```
输出结果：
0   1.787373
1  -0.605159
2   0.180477
3  -0.140922
dtype: float64

The actual data series is:
[ 1.78737302 -0.60515881 0.18047664 -0.1409218 ]
```

## head()和tail()方法示例
```
head()返回前n行(观察索引值)。要显示的元素的默认数量为5，但可以传递自定义这个数字值。
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print ("The original series is:")
print s

print ("The first two rows of the data series:")
print s.head(2)
```
```
输出结果：
The original series is:
0   0.720876
1  -0.765898
2   0.479221
3  -0.139547
dtype: float64

The first two rows of the data series:
0   0.720876
1  -0.765898
dtype: float64
```
```
tail()返回最后n行(观察索引值)。 要显示的元素的默认数量为5，但可以传递自定义数字值
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print ("The original series is:")
print s

print ("The last two rows of the data series:")
print s.tail(2)
```
```
输出结果：
The original series is:
0 -0.655091
1 -0.881407
2 -0.608592
3 -2.341413
dtype: float64

The last two rows of the data series:
2 -0.608592
3 -2.341413
dtype: float64
```


# DataFrame基本功能
|编号|属性或方法|描述| 
|:-:|:-:|:-:|
|1|T|转置行和列|









