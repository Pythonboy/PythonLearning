operator模块输出一系列对应Python内部操作符的函数。例如：operator.add(x, y)等价于表达式x+y。许多函数的名称都被一些特定的方法使用，
没有下划线加持。为了向下兼容，它们中的许多都保留着由双下划线的变体。那些不具备双下划线的变体是为了使表达更清晰。

这些函数在各种函数目录里扮演者对相比较、逻辑操作、数学运算以及序列操作等角色。

对于所有对象来讲对象比较函数是十分有用的，并且这些函数以它们支持的丰富的比较操作命名。

operator. lt(a, b)          //less than小于

operator. le(a, b)          //lessthan or equal to小于等于

operator. eq(a, b)          //equal to等于

operator. ne(a, b)          //not equalto不等于

operator. ge(a, b)          //greaterand equal to大于等于

operator. gt(a, b)          //greater大于

operator. __le__(a, b)

operator. __lt__(a, b)

operator. __eq__(a, b)

operator. __ne__(a, b)

operator. __ge__(a, b)

operator. __gt__(a, b)



逻辑操作一般也适用于所有对象，并且支持真值比较、定义测试和布尔操作

operator. not_(obj)

operator. __not__(obj)

返回非obj的结果。（注意：对于对象实例不存在__not__()方法；只有解释器代码定义了这个操作。它的结果受__bool__()和__len__()方法影响）。

operator. truth(obj)

如果obj是真的，就返回True，否则返回False。等价于使用布尔构造器。

operator. is_(a, b)

返回表达式a is b，用于测试对象的定义。

operator. is_not(a, b)

返回表达式a is not b，用于测试对象定义。



数学运算和按位运算是最多的：

operator. abs(obj)
operator. __abs__(obj)
返回obj的绝对值。

operator. add(a, b)
operator. __add__(a, b)
返回a+b，a与b应为数字。

operator. and(a, b)
operator. __and__(a, b)
返回a与b的按位与操作结果。

operator. floordiv(a, b)
operator. __floordiv(a, b)
返回a//b。（a/b向下取整）

operator. index(a)
operator. __index__(a)
将a转换为整数数据并返回。等价于a. __index__()

operator. inv(obj)
operator. invert(obj)
operator. __inv__(obj)
operator. __invert__(obj)
对数字obj按位求反，并返回。等价于~obj。

operator. lshift(a, b)
operator. __lshift__(a, b)
将a左移b位后返回。

operator. mod(a, b)
operator. __mod__(a, b)
返回a%b。 

operator. mul(a, b)
operator. __mul__(a, b)
返回a*b，a与b都为数字。 

operator. matmul(a, b)
operator. __matmul__(a, b)
返回a@b。

operator. nge(obj)
operator. __neg__(obj)
返回obj的负值（-obj）。

operator. or(a, b)
operator. __or__(a, b)
a与b按位求或，并返回结果值。

operator. pos(obj)
operator. __pow__(obj)
返回obj的正值（+obj）。

operator. pow(a, b)
operator. __pow__(a, b)
返回a ** b，a与b都为数字。

operator. rshift(a, b)
operator. __rshift__(a, b)
a右移b位，并返回结果值。

operator. sub(a, b)
operator. __sub__(a, b)
返回a – b。

operator. truediv(a, b)
operator. __truediv__(a, b)
返回a / b，并且类似于2/3是0.66而不是0。它也被称为真除法。

operator. xor(a, b)
operator. __xor__(a, b)
a与b按位异或，并返回结果。



 和序列有关的操作（其中的一些也可用于映射），包括：

operator. concat(a, b)
operator. __concat__(a, b)
返回a + b，a与b都为序列。

operator. contains(a, b)
operator. __contains__(a, b)
返回测试b in a的结果。请注意反转操作数。

operator. countof(a, b)
返回b在a中出现的次数。

operator. delitem(a, b)
operator. __delitem__(a, b)
删除a索引b的值。

operator. getitem(a, b)
operator. __getitem__(a, b)
返回a索引b的值。

operator. indexof(a, b)
返回b在a中第一次出现时的索引。

operator. setitem(a, b, c)
operator. __setitem__(a, b, c)
a中索引b的位置上的值设置为c。

operator. length_hint(obj, default=0)
返回对象obj的估算长度。首先试图返回真实的长度，不行的话使用obj.__length_hint__()估算长度，再不行的话返回默认值规定的长度。







加法

a + b

add(a, b)

连接

seq1 + seq2

concat(seq1, seq2)

包含测试

obj in seq

contains(seq, obj)

除法

a / b

truediv(a, b)

除法

a // b

floordiv(a, b)

按位与

a & b

and_(a, b)

按位异或

a ^ b

xor(a, b)

按位求反

~ a

invert(a)

按位求或

a | b

or_(a, b)

求幂

a ** b

pow(a, b)

身份测试

a is b

is_(a, b)

身份测试

a is not b

is_not(a, b)

索引分配

obj[k] = v

setitem(obj, k, v)

索引删除

del obj[k]

delitem(obj, k)

得出索引键值

obj[k]

getitem(obj, k)

左移

a << b

lshift(a, b)

求模

a % b

mod(a, b)

乘法

a * b

mul(a, b)

矩阵乘法

a @ b

matmul(a, b)

求负值（数学）

- a

neg(a)

求负值（逻辑）

not a

not_(a)

求正值

+ a

pos(a)

右移

a >> b

rshift(a, b)

片段分配

seq[i: j] = values

setitem(seq, slice(I, j), values)

片段删除

del seq[i, j]

delitem(seq, slice(I, j))

得到片段

swq[i : j]

getitme(seq, slice(i, j))

字符串格式化

s % obj

mod(s, obj)

减法

a - b

sub(a, b)

真值测试

obj

truth(obj)

排序

a < b

lt(a, b)

排序

a <= b

le(a, b)

相等

a == b

eq(a, b)

不等

a !- b

ne(a, b)

排序

a >= b

ge(a, b)

排序

a > b

ge(a, b)










