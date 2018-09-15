# Pandas分类数据     
**分类数据类型在以下情况下非常有用**
- 一个字符串变量，只包含几个不同的值。将这样的字符串变量转换为分类变量将会节省一些内存  
- 变量的词汇顺序与逻辑顺序("one"，"two"，"three")不同。 通过转换为分类并指定类别上的顺序，排序和最小/最大将使用逻辑顺序，而不是词法顺序
- 作为其他python库的一个信号，这个列应该被当作一个分类变量(例如，使用合适的统计方法或plot类型)

## 对象创建
**分类对象可以通过多种方式创建**
### 类别分类
**通过在pandas对象创建中将dtype指定为“category”**
```
import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print (s)
```
```
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): [a, b, c]
```

**pd.Categorical**
```
import pandas as pd
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print (cat)
```
```
[a, b, c, a, b, c]
Categories (3, object): [a, b, c]
```

```
import pandas as pd
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print (cat)
```
```
[a, b, c, a, b, c, NaN]
Categories (3, object): [c, b, a]
```
*这里，第二个参数表示类别。因此，在类别中不存在的任何值将被视为NaN*
```
import pandas as pd
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print (cat)
```
```
[a, b, c, a, b, c, NaN]
Categories (3, object): [c < b < a]
```
*从逻辑上讲，排序(ordered)意味着，a大于b，b大于c*

## 描述
**使用分类数据上的.describe()命令，可以得到与类型字符串的Series或DataFrame类似的输出**
```
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})
print (df.describe())
print ("=============================")
print (df["cat"].describe())
```
```
       cat  s
count    3  3
unique   2  2
top      c  c
freq     2  2
=============================
count     3
unique    2
top       c
freq      2
Name: cat, dtype: object
```

### 获取类别的属性
**obj.cat.categories命令用于获取对象的类别**
```
import pandas as pd
import numpy as np
s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (s.categories)
```
```
Index(['b', 'a', 'c'], dtype='object')
```

**obj.ordered命令用于获取对象的顺序**
```
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (cat.ordered)
```
```
False
```

### 重命名类别
**重命名类别是通过将新值分配给series.cat.categories属性来完成的**
```
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]

print (s.cat.categories)
```
```
Index(['Group a', 'Group b', 'Group c'], dtype='object')
```
**初始类别[a，b，c]由对象的s.cat.categories属性更新**

### 添加新类别
**使用Categorical.add.categories()方法，可以追加新的类别**
```
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print (s.cat.categories)
```
```
Index(['a', 'b', 'c', 4], dtype='object')
```

### 删除新类别
**使用Categorical.remove_categories()方法，可以删除不需要的类别**
```
import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print ("Original object:")
print (s)
print("=====================================")
print ("After removal:")
print (s.cat.remove_categories("a"))
```
```
Original object:
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): [a, b, c]
=====================================
After removal:
0    NaN
1      b
2      c
3    NaN
dtype: category
Categories (2, object): [b, c]
```

### 分类数据比较  
在三种情况下可以将分类数据与其他对象进行比较
- 将等号(==和!=)与类别数据相同长度的类似列表的对象(列表，系列，数组…)进行比较。
- 当ordered==True和类别是相同时，所有比较(==，!=，>，>=，<，和<=)分类数据到另一个分类系列。
- 将分类数据与标量进行比较。
```
import pandas as pd
cat = pd.Series([1,2,3]).astype("category", categories=[1,2,3], ordered=True)
cat1 = pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)
print (cat>cat1)
```
```
0    False
1    False
2     True
dtype: bool
```
