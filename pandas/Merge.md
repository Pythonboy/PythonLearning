# Pandas合并/连接     

**Pandas提供了一个单独的merge()函数，作为DataFrame对象之间所有标准数据库连接操作的入口**
```
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,left_index=False, right_index=False, sort=True)
```

|参数|作用|
|:-:|:-:|
|left|一个DataFrame对象|
|right|另一个DataFrame对象|
|on|列(名称)连接，必须在左和右DataFrame对象中存在(找到)|
|left_on|左侧DataFrame中的列用作键，可以是列名或长度等于DataFrame长度的数组|
|right_on|来自右的DataFrame的列作为键，可以是列名或长度等于DataFrame长度的数组|
|left_index|如果为True，则使用左侧DataFrame中的索引(行标签)作为其连接键|
|right_index|同上|
|how|它是left, right, outer以及inner之中的一个，默认为内inner|
|sort|按照字典顺序通过连接键对结果DataFrame进行排序。默认为True，设置为False时，在很多情况下大大提高性能|

**现在创建两个不同的DataFrame并对其执行合并操作**
```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print("========================================")
print (right)
```
```
     Name  id subject_id
0    Alex   1       sub1
1     Amy   2       sub2
2   Allen   3       sub4
3   Alice   4       sub6
4  Ayoung   5       sub5
========================================
    Name  id subject_id
0  Billy   1       sub2
1  Brian   2       sub4
2   Bran   3       sub3
3  Bryce   4       sub6
4  Betty   5       sub5
```

**在一个键上合并两个数据帧**
```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left,right,on='id')
print(rs)
```
```
   Name_x  id subject_id_x Name_y subject_id_y
0    Alex   1         sub1  Billy         sub2
1     Amy   2         sub2  Brian         sub4
2   Allen   3         sub4   Bran         sub3
3   Alice   4         sub6  Bryce         sub6
4  Ayoung   5         sub5  Betty         sub5
```

**合并多个键上的两个数据框**
```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left,right,on=['id','subject_id'])
print(rs)
```
```
   Name_x  id subject_id Name_y
0   Alice   4       sub6  Bryce
1  Ayoung   5       sub5  Betty
```
*(只有同时满足多个列中键值相同时，才会合并在一起）*


**合并使用how参数**
---
**如何合并参数指定如何确定哪些键将被包含在结果表中。如果组合键没有出现在左侧或右侧表中，则连接表中的值将为NA**
|合并方法	|SQL等效	|描述|
|:-:|:-:|:-:|
|left|	LEFT OUTER JOIN|	使用左侧对象的键|
|right|	RIGHT OUTER JOIN|	使用右侧对象的键|
|outer|	FULL OUTER JOIN	|使用键的联合|
|inner|	INNER JOIN|	使用键的交集|

### left join
```
mport pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='left')
print (rs)
```
```
   Name_x  id_x subject_id Name_y  id_y
0    Alex     1       sub1    NaN   NaN
1     Amy     2       sub2  Billy   1.0
2   Allen     3       sub4  Brian   2.0
3   Alice     4       sub6  Bryce   4.0
4  Ayoung     5       sub5  Betty   5.0

```

### right join   
```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='right')
print (rs)
```
```
  Name_x  id_x subject_id Name_y  id_y
0     Amy   2.0       sub2  Billy     1
1   Allen   3.0       sub4  Brian     2
2   Alice   4.0       sub6  Bryce     4
3  Ayoung   5.0       sub5  Betty     5
4     NaN   NaN       sub3   Bran     3
```

### outer join  
```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, how='outer', on='subject_id')
print (rs)
```
```
  Name_x  id_x subject_id Name_y  id_y
0    Alex   1.0       sub1    NaN   NaN
1     Amy   2.0       sub2  Billy   1.0
2   Allen   3.0       sub4  Brian   2.0
3   Alice   4.0       sub6  Bryce   4.0
4  Ayoung   5.0       sub5  Betty   5.0
5     NaN   NaN       sub3   Bran   3.0
```

### inner join   
**连接将在索引上进行。连接(Join)操作将授予它所调用的对象。所以，a.join(b)不等于b.join(a)**
```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='inner')
print (rs)
```
```
   Name_x  id_x subject_id Name_y  id_y
0     Amy     2       sub2  Billy     1
1   Allen     3       sub4  Brian     2
2   Alice     4       sub6  Bryce     4
3  Ayoung     5       sub5  Betty     5
```

























