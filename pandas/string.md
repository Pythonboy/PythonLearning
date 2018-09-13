# Pandas字符串与文本   
Pandas提供了一组字符串函数，可以方便地对字符串数据进行操作。 最重要的是，这些函数忽略(或排除)丢失/NaN值。

## lower()   
**将Series/Index中的字符串转换为小写**
```
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print (s.str.lower())
```

```
0             tom
1    william rick
2            john
3         alber@t
4             NaN
5            1234
6      steveminsu
dtype: object
```


## upper()   
**将Series/Index中的字符串转换为大写。**
```
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print (s.str.upper())
```
```
0             TOM
1    WILLIAM RICK
2            JOHN
3         ALBER@T
4             NaN
5            1234
6      STEVESMITH
dtype: object
```

## len()
**计算字符串长度**
```
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])
print (s.str.len())
```

```
0     3.0
1    12.0
2     4.0
3     7.0
4     NaN
5     4.0
6    10.0
dtype: float64
```

## strip()
**帮助从两侧的系列/索引中的每个字符串中删除空格(包括换行符)**
```
import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("=========== After Stripping ================")
print (s.str.strip())
```

```
0             Tom 
1     William Rick
2             John
3          Alber@t
dtype: object
=========== After Stripping ================
0             Tom
1    William Rick
2            John
3         Alber@t
dtype: object
```

## split()
**用给定的模式拆分每个字符串**
```
import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("================= Split Pattern: ==================")
print (s.str.split(' '))
```

```
0             Tom 
1     William Rick
2             John
3          Alber@t
dtype: object
================= Split Pattern: ==================
0              [Tom, ]
1    [, William, Rick]
2               [John]
3            [Alber@t]
dtype: object
```

## cat()  
**使用给定的分隔符连接系列/索引元素**
```
import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.cat(sep=' <=> '))
```

```
Tom  <=>  William Rick <=> John <=> Alber@t
```

## get_dummies()
**返回具有单热编码值的数据帧(DataFrame)**
```
import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.get_dummies())
```

```
    William Rick  Alber@t  John  Tom 
0              0        0     0     1
1              1        0     0     0
2              0        0     1     0
3              0        1     0     0
```

## contains()
**如果元素中包含子字符串，则返回每个元素的布尔值True，否则为False**
```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.contains(' '))
```
```
0     True
1     True
2    False
3    False
dtype: bool
```

## replace(a,b)
**将值a替换为值b**
```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("After replacing @ with $: ============== ")
print (s.str.replace('@','$'))
```

```
0             Tom 
1     William Rick
2             John
3          Alber@t
dtype: object
After replacing @ with $: ============== 
0             Tom 
1     William Rick
2             John
3          Alber$t
dtype: object
```

## repeat()
**重复每个元素指定的次数**
```
mport pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.repeat(2))
```

```
0                      Tom Tom 
1     William Rick William Rick
2                      JohnJohn
3                Alber@tAlber@t
dtype: object
```

## count()   
**返回模式中每个元素的出现总数**
```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("The number of 'm's in each string:")
print (s.str.count('m'))
```

```
The number of 'm's in each string:
0    1
1    1
2    0
3    0
dtype: int64
```

## startwith()
**如果系列/索引中的元素以模式开始，则返回true**
```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("Strings that start with 'T':")
print (s.str. startswith ('T'))
```

```
Strings that start with 'T':
0     True
1    False
2    False
3    False
dtype: bool
```


## endwith()
**如果系列/索引中的元素以模式结束，则返回true**
```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("Strings that end with 't':")
print (s.str.endswith('t'))
```

```
Strings that end with 't':
0    False
1    False
2    False
3     True
dtype: bool
```

## find()   
**返回模式第一次出现的位置**
```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.find('e'))
```

```
0   -1
1   -1
2   -1
3    3
dtype: int64
```


## findall()   
**返回模式的所有出现的列表**
```
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.findall('e'))
```

```
0     []
1     []
2     []
3    [e]
dtype: object
```
*空列表([])表示元素中没有这样的模式可用*


## swapcase()
**变换字母大小写**
```
import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.swapcase())
```

```
0             tOM
1    wILLIAM rICK
2            jOHN
3         aLBER@T
dtype: object
```


## islower()
**检查系列/索引中每个字符串中的所有字符是否小写，返回布尔值**
```
import pandas as pd
s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.islower())
```

```
0    False
1    False
2    False
3    False
dtype: bool
```


## isupper()  
**检查系列/索引中每个字符串中的所有字符是否大写，返回布尔值**
```
import pandas as pd
s = pd.Series(['TOM', 'William Rick', 'John', 'Alber@t'])
print (s.str.isupper())
```

```
0    True
1    False
2    False
3    False
dtype: bool
```


## isnumeric() 
**检查系列/索引中每个字符串中的所有字符是否为数字，返回布尔值**
```
import pandas as pd
s = pd.Series(['Tom', '1199','William Rick', 'John', 'Alber@t'])
print (s.str.isnumeric())
```

```
0    False
1     True
2    False
3    False
4    False
dtype: bool
```
