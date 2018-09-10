decimal 模块
简介：decimal意思为十进制，这个模块提供了十进制浮点运算支持。
小数值表示为 Decimal 类的实例。构造函数取一个整数或字符串作为参数。使用浮点数创建 Decimal 之前，可以先将浮点数转换为一个字符串，使调用者能够显式地处理值得位数，倘若使用硬件浮点数表示则无法准确地表述。另外，利用类方法 from_float() 可以转换为精确的小数表示。
模块方法
导入模块　语法： from decimal import *

方法名	描述
localcontext	
getcontext	使用一个上下文（context）覆盖某些设置，如保持精度、如何完成取整、错误处理等等。上下文可以应用于一个线程中的所有 Decimal 实例，或者局部应用于一个小代码区。
from_float()	可以转换为精确的小数表示。

decimal的context：
decimal在一个独立的context下工作，可以通过getcontext来获取当前环境。可以通过decimal.getcontext().prec来设定小数点精度（默认为28）

from decimal import *

getcontext().prec = 2

tmp = Decimal(float(2551.179))-Decimal(float(2551.178))
print tmp

#结果默认从小数的1开始保留两位
0.0010
[Finished in 0.6s]

从浮点型转换为Decimal类型
from decimal import *

a = 2542851.1739
tmp = Decimal.from_float(a)
print tmp

#Decimal类型   高精度数据
2542851.173899999819695949554443359375
[Finished in 0.7]

留在最后的话
如果a等于b，Decimal(a)-Decimal(b) ,得到的是0E-30，而不是0 
将无法比较，建议转换float类型进行减法
