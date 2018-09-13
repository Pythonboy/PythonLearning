# Pandas函数应用

要将自己或其他库的函数应用于Pandas对象，应该了解三种重要的方法。以下讨论了这些方法。 使用适当的方法取决于函数是否期望在整个DataFrame，
行或列或元素上进行操作。

- 表明智函数应用：pipe()
- 行或列函数应用：apply()
- 元素函数应用：applymap()

## 表格函数应用  
可以通过将函数和适当数量的参数作为管道参数来执行自定义操作。 因此，对整个DataFrame执行操作

例如，为DataFrame中的所有元素相加一个值2
**加法器函数**
```
def adder(ele1,ele2):
  return ele1+ele2
```
```
import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print df
```
```
输出结果：
        col1       col2       col3
0   2.176704   2.219691   1.509360
1   2.222378   2.422167   3.953921
2   2.241096   1.135424   2.696432
3   2.355763   0.376672   1.182570
4   2.308743   2.714767   2.130288
```

## 行或列智能函数应用
可以使用apply()方法沿DataFrame或Panel的轴应用任意函数，它与描述性统计方法一样，采用可选的轴参数

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print df
```
```
输出结果：
      col1       col2        col3                                                      
0   0.343569  -1.013287    1.131245 
1   0.508922  -0.949778   -1.600569 
2  -1.182331  -0.420703   -1.725400
3   0.860265   2.069038   -0.537648
4   0.876758  -0.238051    0.473992
```


```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
print df
```
```
     col1         col2         col3
0  0.543255    -1.613418    -0.500731   
1  0.976543    -1.135835    -0.719153   
2  0.184282    -0.721153    -2.876206    
3  0.447738     0.268062    -1.937888
4 -0.677673     0.177455     1.397360
```


```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x: x.max() - x.min())
print df
```
```
       col1        col2      col3
0   -0.585206   -0.104938   1.424115 
1   -0.326036   -1.444798   0.196849 
2   -2.033478    1.682253   1.223152  
3   -0.107015    0.499846   0.084127
4   -1.046964   -1.935617  -0.009919
```

## 元素智能函数应用
并不是所有的函数都可以向量化(也不是返回另一个数组的NumPy数组，也不是任何值)，在DataFrame上的方法applymap()和类似地在Series上的map()
接受任何Python函数，并且返回单个值

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
df['col1'].map(lambda x:x*100)
print df
```
```
输出结果：
       col1      col2       col3    
0    0.629348  0.088467  -1.790702 
1   -0.592595  0.184113  -1.524998
2   -0.419298  0.262369  -0.178849
3   -1.036930  1.103169   0.941882 
4   -0.573333 -0.031056   0.315590
```

```
import pandas as pd
import numpy as np
# My custom function
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
print df
```
```
output is as follows:
         col1         col2         col3
0   17.670426    21.969052    -49.064031
1   22.237846    42.216693     195.392124
2   24.109576   -86.457646     69.643171
3   35.576312   -162.332803   -81.743023
4   30.874333    71.476717     13.028751
```

