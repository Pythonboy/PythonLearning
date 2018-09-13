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
|2|axes|返回一个列，行轴标签和列轴标签作为唯一的成员|
|3|dtypes|返回此对象中的数据类型(dtypes)|
|4|empty|如果NDFrame完全为空[无项目]，则返回为True; 如果任何轴的长度为0|
|5|ndim|轴/数组维度大小|
|6|shape|返回表示DataFrame的维度的元组|
|7|size|NDFrame中的元素数|
|8|values|NDFrame的Numpy表示|
|9|head()|返回开头前n行|
|10|tail()|返回最后n行|

**示例**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print df
```
```
Our data series is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80
```

## T
**返回DataFrame的转置。行和列将交换**
```
import pandas as pd
import numpy as np
# Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# Create a DataFrame
df = pd.DataFrame(d)
print ("The transpose of the data series is:")
print df.T
```
```
The transpose of the data series is:
         0     1       2      3      4      5       6
Age      25    26      25     23     30     29      23
Name     Tom   James   Ricky  Vin    Steve  Minsu   Jack
Rating   4.23  3.24    3.98   2.56   3.2    4.6     3.8
```

## axes
**返回行轴标签和列轴标签列表**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Row axis labels and column axis labels are:")
print df.axes
```
```
Row axis labels and column axis labels are:
[RangeIndex(start=0, stop=7, step=1), Index([u'Age', u'Name', u'Rating'],
dtype='object')]
```

## dtypes
**返回每列的数据类型**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("The data types of each column are:")
print df.dtypes
```
```
The data types of each column are:
Age     int64
Name    object
Rating  float64
dtype: object
```

## empty
**返回布尔值，表示对象是否为空; 返回True表示对象为空**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Is the object empty?")
print df.empty
```
```
Is the object empty?
False
```

## ndim
**返回对象的维数。根据定义，DataFrame是一个2D对象**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The dimension of the object is:")
print df.ndim
```
```
Our object is:
      Age    Name     Rating
0     25     Tom      4.23
1     26     James    3.24
2     25     Ricky    3.98
3     23     Vin      2.56
4     30     Steve    3.20
5     29     Minsu    4.60
6     23     Jack     3.80

The dimension of the object is:
2
```

## shape
**返回表示DataFrame的维度的元组。 元组(a，b)，其中a表示行数，b表示列数**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The shape of the object is:")
print df.shape
```
```
Our object is:
   Age   Name    Rating
0  25    Tom     4.23
1  26    James   3.24
2  25    Ricky   3.98
3  23    Vin     2.56
4  30    Steve   3.20
5  29    Minsu   4.60
6  23    Jack    3.80

The shape of the object is:
(7, 3)
```

## size
**返回DataFrame中的元素数**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The total number of elements in our object is:")
print df.size
```
```
Our object is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80

The total number of elements in our object is:
21
```

## values
**将DataFrame中的实际数据作为NDarray返回**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The actual data in our data frame is:")
print df.values
```
```
Our object is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80
The actual data in our data frame is:
[[25 'Tom' 4.23]
[26 'James' 3.24]
[25 'Ricky' 3.98]
[23 'Vin' 2.56]
[30 'Steve' 3.2]
[29 'Minsu' 4.6]
[23 'Jack' 3.8]]
```

## head()
**返回最前面的n行，默认返回5行**
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data frame is:")
print df
print ("The first two rows of the data frame is:")
print df.head(2)
```
```
Our data frame is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80

The first two rows of the data frame is:
   Age   Name   Rating
0  25    Tom    4.23
1  26    James  3.24
```

## tail()
**返回最后的n行，默认返回5行
```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]), 
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data frame is:")
print df
print ("The last two rows of the data frame is:")
print df.tail(2)
```
```
Our data frame is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80

The last two rows of the data frame is:
    Age   Name    Rating
5   29    Minsu    4.6
6   23    Jack     3.8
```

























