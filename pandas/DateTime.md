# Pandas日期功能
**日期功能扩展了时间序列，在财务数据分析中起主要作用。在处理日期数据的同时，我们经常会遇到以下情况**
- 生成日期序列
- 将日期序列转换为不同的频率

## 创建一个日期范围  
**通过指定周期和频率，使用date.range()函数就可以创建日期序列。 默认情况下，范围的频率是天**
```
import pandas as pd
datelist = pd.date_range('2020/11/21', periods=5)
print(datelist)
```
```
DatetimeIndex(['2020-11-21', '2020-11-22', '2020-11-23', '2020-11-24',
               '2020-11-25'],
              dtype='datetime64[ns]', freq='D')
```

### 更改时间频率   
```
import pandas as pd
datelist = pd.date_range('2020/11/21', periods=5,freq='M')
print(datelist)
```
```
DatetimeIndex(['2020-11-30', '2020-12-31', '2021-01-31', '2021-02-28',
               '2021-03-31'],
              dtype='datetime64[ns]', freq='M')
```


## bdate_range()
**bdate_range()用来表示商业日期范围，不同于date_range()，它不包括星期六和星期天**
```
import pandas as pd
datelist = pd.bdate_range('2011/11/03', periods=5)
print(datelist)
```
```
DatetimeIndex(['2017-11-03', '2017-11-06', '2017-11-07', '2017-11-08',
               '2017-11-09'],
              dtype='datetime64[ns]', freq='B')
```


**像date_range和bdate_range这样的便利函数利用了各种频率别名。date_range的默认频率是日历中的自然日，而bdate_range的默认频率是工作日**
```
import pandas as pd
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
dates = pd.date_range(start, end)
print(dates)
```
```
DatetimeIndex(['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04',
               '2017-11-05'],
              dtype='datetime64[ns]', freq='D')
```




