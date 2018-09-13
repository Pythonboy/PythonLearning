# 系列基本功能   
- axes : 返回行轴标签列表
- dtype ：返回对象的数据类型(dtype)
- empty ： 如果系列为空，则返回True
- ndim ： 返回底层数据的维数，默认定义：1
- size ： 返回基础数据中的元素数
- values ： 将系列作为ndarray返回
- head() : 返回前n行
- tail() : 返回最后n行


# axes示例
'''
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print s
'''

**输出结果**
'''
0   0.967853
1  -0.148368
2  -1.395906
3  -1.758394
dtype: float64
'''
