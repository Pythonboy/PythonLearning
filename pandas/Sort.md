# Pandas排序

**Pandas有两种排序方式，它们分别是**
- **按标签**
- **按实际值**

```
import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
mns=['col2','col1'])
print (unsorted_df)
```
```
       col2      col1
1  1.069838  0.096230
4 -0.542406 -0.219829
6 -0.071661  0.392091
2  1.399976 -0.472169
3  0.428372 -0.624630
5  0.471875  0.966560
9 -0.131851 -1.254495
8  1.180651  0.199548
0  0.906202  0.418524
7  0.124800  2.011962
```

## 按标签排序  
使用**sort_index()**方法，通过传递axis参数和排序顺序，可以对DataFrame进行排序。 默认情况下，按照升序对行标签进行排序

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df=unsorted_df.sort_index()
print (sorted_df)
```
```
       col2      col1
0  0.431384 -0.401538
1  0.111887 -0.222582
2 -0.166893 -0.237506
3  0.476472  0.508397
4  0.670838  0.406476
5  2.065969 -0.324510
6 -0.441630  1.060425
7  0.735145  0.972447
8 -0.051904 -1.112292
9  0.134108  0.759698
```

## 排序顺序  
通过将布尔值传递给升序参数，可以控制排序顺序
```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)
```
```
       col2      col1
9  0.750452  1.754815
8  0.945238  2.079394
7  0.345238 -0.162737
6 -0.512060  0.887094
5  1.163144  0.595402
4 -0.063584 -0.185536
3 -0.275438 -2.286831
2 -1.504792 -1.222394
1  1.031234 -1.848174
0 -0.615083  0.784086
```

## 按列排序  
通过传递axis参数值为0或1，可以对列标签进行排序。 默认情况下，axis = 0，逐行排列
```
import pandas as pd
import numpy as np
unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])
sorted_df=unsorted_df.sort_index(axis=1)
print (sorted_df)
```
```
       col1      col2
1 -0.997962  0.736707
4  1.196464  0.703710
6 -0.387800  1.207803
2  1.614043  0.356389
3 -0.057181 -0.551742
5  1.034451 -0.731490
9 -0.564355  0.892203
8 -0.763526  0.684207
0 -1.213615  1.268649
7  0.316543 -1.450784
```

## 按值排序
像索引排序一样，**sort_values()**是按值排序的方法。它接受一个by参数，它将使用要与其排序值的DataFrame的列名称
```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1')

print (sorted_df)
```
```
   col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
```
*观察上面的输出结果，col1值被排序，相应的col2值和行索引将随col1一起改变。因此，它们看起来没有排序*

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by=['col1','col2'])

print (sorted_df)
```
```
   col1  col2
2     1     2
1     1     3
3     1     4
0     2     1
```

## 排序算法   
**sort_values()**提供了从**mergeesort**，**heapsort**和**quicksort**中选择算法的一个配置。Mergesort是唯一稳定的算法

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')

print (sorted_df)
```
```
   col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
```



