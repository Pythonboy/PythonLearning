它提供了数学函数在复数域上扩展的运算函数，math模块内的函数属于其子集，该模块是为了某些需要在复数域上进行的操作站门设计的。该模块的函数
允许复数、整数、浮点数等数据类型的输入。如无特殊说明，所有函数的返回值都应当为实部、虚部皆为浮点数的复数。

1 极坐标与直角坐标的相互转换函数

       在Python中，复数使用矩阵或笛卡尔坐标结构来保存数据；其完整结构应当包含实部和虚部两部分。用表达式表示如下：

              Z== Z. real + Z. imag*j

       极坐标的存在使得复数又获得了一种新的表示形式。在极坐标中，复数Z由系数r和相位角phi两者合作定义。系数r指的是复数Z在坐标系中离坐标原点的距离，相位角phi是以弧度为单位测量的从正x轴到将原点连接到z的线段的逆时针角度。

       以下函数可以提供直角坐标与极坐标的相互转换：

cmath.phase(x)

       返回x的相位。如果x是浮点数，其等价于math. atan2(x.imag, x.real)。结果范围在正负ℼ之间。

 

cmath. polar(x)

       返回x的极坐标表达形式（r, phi）。（r, phi）等价于（abs(x), phase(x)）。

 

cmath. rect(r,phi)

       用(r,phi)构建一个复数，并将其返回。

 

2.指数函数和对数函数

cmath. exp(x)

       返回e**x的结果值。

 

cmath. log(x, [base])

       对x求base指定底的对数运算，并返回结果值。如果base没有给出，其默认为e。有一个分支从0开始沿负实轴旋转到-∞，从上向下连续。

 

cmath. log10(x)

       求x以10为底的对数。分支与log()相同。

 

 

cmath. sqrt(x)

       返回x的平方根。分支与log()相同。

 

3. 三角函数

cmath. acos(x)

       返回x的反余弦值。这里有两个分支切口：一个从实轴向右延伸到∞，从下面连续。 另一个从实轴-1从左向上延伸到-∞，从上面连续。

 

cmath. asin(x)

       返回x的反正弦值。分支切口与acos()相同。

 

cmath. atan(x)

       返回x的反正切值。分支切口与acos()相同。

 

cmath. cos()

       返回x的余弦值。

 

cmath. sin(x)

       返回x的正弦值。

 

cmath. tan()

       返回x的正切值。

 

4. 双曲函数

cmath. acosh(x)

       返回x的反双曲余弦值。这里有一个分支切口，从实轴的1向左延伸到-∞，从上面连续。

 

cmath. asinh(x)

       返回x的反双曲正弦值。这里有两个分支切口：一个是沿着虚轴从1j向右到∞j，另一个是沿着虚轴从-1j向左到-∞j。

 

cmath. atanh(x)

       返回x的反双曲正切值。这里有两个分支切口：一个是沿着实轴下方从1到∞，另一个是沿着实轴上方从-1到-∞。

 

cmath. cosh(x)

       返回x的双曲余弦值。

 

cmath. sinh(x)

       返回x的双曲正弦值。

 

cmath. tanh(x)

       返回x的双曲正切值。

 

5.分类函数

cmath. isfinite(x)

       如果x的实部和虚部都是有限数，返回True，否则返回False。

 

cmath. isinf(x)

       如果x的实部或虚部为无穷数，返回True，否则返回False。

 

cmath. isnan(x)

       如果x的实部或虚部是NaN，返回True。

 

cmath. isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

       如果a与b的值之差在规定的范围内，返回True，否则返回False。

rel_tol和abs_tol是误差的相对容许范围和绝对容许范围，实际运算中，误差符合两者中的任意一个即为符合要求。

 

6.常量

cmath. pi

       浮点数形式的圆周率常量。

 

cmath. e

       浮点数形式的自然数e。

 

cmath. tau

       浮点数形式的数学常量τ。

 

cmath. inf

       浮点形式的正无穷。

 

cmath. infj

       实部为0，虚部为正无穷的复数。

 

cmath. nan

       浮点形式的非数字值。

 

cmath. nanj

       实部为0，虚部为NaN的复数。

















