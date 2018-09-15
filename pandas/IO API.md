# Pandas IO 工具   
**Pandas I/O API是一套像pd.read_csv()一样返回Pandas对象的顶级读取器函数。**
**读取文本文件(或平面文件)的两个主要功能是read_csv()和read_table()。它们都使用相同的解析代码来智能地将表格数据转换为DataFrame对象**
```
pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
```
```
pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
```

## read_csv   
**read.csv从csv文件中读取数据并创建一个DataFrame对象**
```
import pandas as pd
df=pd.read_csv("temp.csv")
print (df)
```
```
   S.No    Name  Age       City  Salary
0     1     Tom   28    Toronto   20000
1     2     Lee   32   HongKong    3000
2     3  Steven   43   Bay Area    8300
3     4     Ram   38  Hyderabad    3900
```

## 自定义索引  
**可以指定csv文件中的一列来使用index_col定制索引**
```
import pandas as pd
df=pd.read_csv("temp.csv",index_col=['S.No'])
print (df)
```
```
       Name  Age       City  Salary
S.No                                
1        Tom   28    Toronto   20000
2        Lee   32   HongKong    3000
3     Steven   43   Bay Area    8300
4        Ram   38  Hyderabad    3900
```

## 转换器
**dtype的列可以作为字典传递**
```
import pandas as pd
import numpy as np
df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print (df.dtypes)
```
```
S.No        int64
Name       object
Age         int64
City       object
Salary    float64
dtype: object
```

## header_name  
**使用names参数指定标题的名称**
```
import pandas as pd
import numpy as np
df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e'])
print (df)
```
```
      a       b    c          d       e
0  S.No    Name  Age       City  Salary
1     1     Tom   28    Toronto   20000
2     2     Lee   32   HongKong    3000
3     3  Steven   43   Bay Area    8300
4     4     Ram   38  Hyderabad    3900
```

观察可以看到，标题名称附加了自定义名称，但文件中的标题还没有被消除。 现在，使用header参数来删除它。
如果标题不是第一行，则将行号传递给标题。这将跳过前面的行

```
import pandas as pd
import numpy as np
df=pd.read_csv("temp.csv",names=['a','b','c','d','e'],header=0)
print (df)
```
```
   a       b   c          d      e
0  1     Tom  28    Toronto  20000
1  2     Lee  32   HongKong   3000
2  3  Steven  43   Bay Area   8300
3  4     Ram  38  Hyderabad   3900
```

## skiprows  
**skiprows跳过指定的行数**
```
import pandas as pd
import numpy as np
df=pd.read_csv("temp.csv", skiprows=2)
print (df)
```
```
   2     Lee  32   HongKong  3000
0  3  Steven  43   Bay Area  8300
1  4     Ram  38  Hyderabad  3900
```
















































