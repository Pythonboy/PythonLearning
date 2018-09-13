# Pandas选项和自定义   
Pandas提供API来自定义其行为的某些方面，大多使用来显示。   
API由五个相关函数组成。它们分别是 ： 
- get_option()
- set_option()
- reset_option()
- describe_option()
- option_context()

## get_option()   
**get_option(param)需要一个参数，并返回下面输出中给出的值**
### display.max_rows   
```
import pandas as pd
print ("display.max_rows = ", pd.get_option("display.max_rows"))
```
```
display.max_rows =  60
```
### display.max_columns
```
import pandas as pd
print ("display.max_columns = ", pd.get_option("display.max_columns"))
```
```
display.max_columns =  20
```

## set_option(param,value)   
**set_option需要两个参数，并将该值设置为指定的参数值**
### display.max_rows
```
mport pandas as pd
print ("before set display.max_rows = ", pd.get_option("display.max_rows")) 
pd.set_option("display.max_rows",80)
print ("after set display.max_rows = ", pd.get_option("display.max_rows"))
```
```
before set display.max_rows =  60
after set display.max_rows =  80
```
### display.max_columns
```
import pandas as pd
print ("before set display.max_columns = ", pd.get_option("display.max_columns")) 
pd.set_option("display.max_columns",32)
print ("after set display.max_columns = ", pd.get_option("display.max_columns"))
```
```
before set display.max_columns =  20
after set display.max_columns =  32
```

## reset_option(param)  
**reset_option接受一个参数，并将该值设置为默认值。**
### display.max_rows 
```
import pandas as pd
pd.set_option("display.max_rows",32)
print ("after set display.max_rows = ", pd.get_option("display.max_rows")) 
pd.reset_option("display.max_rows")
print ("reset display.max_rows = ", pd.get_option("display.max_rows"))
```
```
after set display.max_rows =  32
reset display.max_rows =  60
```

## describe_option(param)  
**describe_option打印参数的描述**
```
import pandas as pd
pd.describe_option("display.max_rows")
```
```
display.max_rows : int
    If max_rows is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.

    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 60] [currently: 60]
```

## option_context()  
**option_context上下文管理器用于临时设置语句中的选项。当退出使用块时，选项值将自动恢复**
### display.max_rows
```
import pandas as pd
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))

```
```
10
10
```
*请参阅第一和第二个打印语句之间的区别。第一个语句打印由option_context()设置的值，该值在上下文中是临时的。在使用上下文之后，
第二个打印语句打印配置的值*  

|编号|参数|描述|
|:-:|:-:|:-:|
|1|	display.max_rows|要显示的最大行数|
|2|	display.max_columns	|要显示的最大列数|
|3|	display.expand_frame_repr	|显示数据帧以拉伸页面|
|4|	display.max_colwidth|	显示最大列宽|
|5|	display.precision|	显示十进制数的精度|



