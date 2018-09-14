# Pandas时间差   
**时间差(Timedelta)是时间上的差异，以不同的单位来表示。例如：日，小时，分钟，秒。它们可以是正值，也可以是负值。
可以使用各种参数创建Timedelta对象**

## 字符串   
```
import pandas as pd

timediff = pd.Timedelta('2 days 2 hours 15 minutes 30 seconds')
print(timediff)
```
```
2 days 02:15:30
```

## 整数   
**通过传递一个整数值与指定单位，这样的一个参数也可以用来创建Timedelta对象**
```
import pandas as pd
timediff = pd.Timedelta(6,unit='h')
print(timediff)
```
```
0 days 06:00:00
```

## 数据偏移
**例如 - 周，天，小时，分钟，秒，毫秒，微秒，纳秒的数据偏移也可用于构建**
```
import pandas as pd
timediff = pd.Timedelta(days=2)
print(timediff)
```
```
2 days 00:00:00
```

## 数据运算
**可以在Series/DataFrames上执行运算操作，并通过在datetime64 [ns]系列或在时间戳上减法操作来构造timedelta64 [ns]系列**
```
import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print(df)
```
```
           A      B
0 2012-01-01 0 days
1 2012-01-02 1 days
2 2012-01-03 2 days
```

### 相加操作
```
import pandas as pd

s = pd.Series(pd.date_range('2018-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
print(df)
```
```
           A      B          C
0 2018-01-01 0 days 2018-01-01
1 2018-01-02 1 days 2018-01-03
2 2018-01-03 2 days 2018-01-05
```

### 相减操作
```
import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']-df['B']
print(df)
```
```
           A      B          C          D
0 2018-01-01 0 days 2018-01-01 2018-01-01
1 2018-01-02 1 days 2018-01-03 2018-01-02
2 2018-01-03 2 days 2018-01-05 2018-01-03
```






