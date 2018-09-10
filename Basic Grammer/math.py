 math.e	 自然常数e	 
 >>> math.e
2.718281828459045


 math.pi	 圆周率pi	 
 >>> math.pi
3.141592653589793


 math.degrees(x)	 弧度转度	 
 >>> math.degrees(math.pi)
180.0


 math.radians(x)	 度转弧度	 
 >>> math.radians(45)
0.7853981633974483


 math.exp(x)	 返回e的x次方	 
 >>> math.exp(2)
7.38905609893065


 math.expm1(x)	 返回e的x次方减1	 
 >>> math.expm1(2)
6.38905609893065


 math.log(x[, base])	 返回x的以base为底的对数，base默认为e	 
 >>> math.log(math.e)
1.0
>>> math.log(2, 10)
0.30102999566398114


math.log10(x)	 返回x的以10为底的对数	
>>> math.log10(2)
0.30102999566398114


 math.log1p(x)	 返回1+x的自然对数（以e为底）	 
 >>> math.log1p(math.e-1)
1.0


 math.pow(x, y)	 返回x的y次方	 
 >>> math.pow(5,3)
125.0


 math.sqrt(x)	 返回x的平方根	 
 >>> math.sqrt(3)
1.7320508075688772


 math.ceil(x)	 返回不小于x的整数	 
 >>> math.ceil(5.2)
6.0


 math.floor(x)	 返回不大于x的整数	 
 >>> math.floor(5.8)
5.0


 math.trunc(x)	 返回x的整数部分	 
 >>> math.trunc(5.8)
5


 math.modf(x)	 返回x的小数和整数	 
 >>> math.modf(5.2)
(0.20000000000000018, 5.0)


 math.fabs(x)	 返回x的绝对值	 
 >>> math.fabs(-5)
5.0


 math.fmod(x, y)	 返回x%y（取余）	 
 >>> math.fmod(5,2)
1.0


 math.fsum([x, y, ...])	 返回无损精度的和	 
 >>> 0.1+0.2+0.3
0.6000000000000001
>>> math.fsum([0.1, 0.2, 0.3])
0.6


 math.factorial(x)	 返回x的阶乘	 
 >>> math.factorial(5)
120


 math.isinf(x)	 若x为无穷大，返回True；否则，返回False	 
 >>> math.isinf(1.0e+308)
False
>>> math.isinf(1.0e+309)
True


 math.isnan(x)	 若x不是数字，返回True；否则，返回False	 
 >>> math.isnan(1.2e3)
False


 math.hypot(x, y)	 返回以x和y为直角边的斜边长	 
 >>> math.hypot(3,4)
5.0


 math.copysign(x, y)	 若y<0，返回-1乘以x的绝对值；否则，返回x的绝对值	 
 >>> math.copysign(5.2, -1)
-5.2


 math.frexp(x)	 返回m和i，满足m乘以2的i次方	 
 >>> math.frexp(3)
(0.75, 2)


 math.ldexp(m, i)	 返回m乘以2的i次方	 
 >>> math.ldexp(0.75, 2)
3.0


 math.sin(x)	 返回x（弧度）的三角正弦值	 >>> math.sin(math.radians(30))
0.49999999999999994


 math.asin(x)	 返回x的反三角正弦值	 
 >>> math.asin(0.5)
0.5235987755982989


 math.cos(x)	 返回x（弧度）的三角余弦值	 
 >>> math.cos(math.radians(45))
0.7071067811865476


 math.acos(x)	 返回x的反三角余弦值	 
 >>> math.acos(math.sqrt(2)/2)
0.7853981633974483


 math.tan(x)	 返回x（弧度）的三角正切值	 
 >>> math.tan(math.radians(60))
1.7320508075688767


 math.atan(x)	 返回x的反三角正切值	 
 >>> math.atan(1.7320508075688767)
1.0471975511965976


 math.atan2(x, y)	 返回x/y的反三角正切值	 
 >>> math.atan2(2,1)
1.1071487177940904


 math.sinh(x)	 返回x的双曲正弦函数	 
 
 math.asinh(x)	 返回x的反双曲正弦函数	
 
 math.cosh(x)	 返回x的双曲余弦函数	 
 
 math.acosh(x)	 返回x的反双曲余弦函数	 
 
 math.tanh(x)	 返回x的双曲正切函数	 
 
 math.atanh(x)	 返回x的反双曲正切函数	 
 
 math.erf(x)	 返回x的误差函数	 
 
 math.erfc(x)	 返回x的余误差函数	 
 
 math.gamma(x)	 返回x的伽玛函数	 
 
 math.lgamma(x)	 返回x的绝对值的自然对数的伽玛函数	 
 
