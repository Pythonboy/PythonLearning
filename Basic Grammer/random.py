1.random 模块的基本方法

import random
 
print(random.random())          #随机产生[0,1)之间的浮点值
print(random.randint(1,6))      #随机生成指定范围[a,b]的整数
print(random.randrange(1,3))    #随机生成指定范围[a,b)的整数
print(random.randrange(0,101,2))  ##随机生成指定范围[a,b)的指定步长的数（2--偶数）
print(random.choice("hello"))  #随机生成指定字符串中的元素
print(random.choice([1,2,3,4])) #随机生成指定列表中的元素
print(random.choice(("abc","123","liu")))  #随机生成指定元组中的元素
print(random.sample("hello",3))    #随机生成指定序列中的指定个数的元素
print(random.uniform(1,10))     #随机生成指定区间的浮点数
 
#洗牌
items = [1,2,3,4,5,6,7,8,9,0]
print("洗牌前:",items)
random.shuffle(items)
print("洗牌后:",items)


洗牌前: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
洗牌后: [6, 9, 2, 7, 1, 3, 8, 5, 4, 0]


2、random模块中方法的实际应用——生成随机验证码
（1）随机生成4位纯数字验证码
import random
check_code = ''   #最终生成的验证码
for i in range(4):       #4位长的纯数字验证码
    cur = random.randint(0,9)
    check_code += str(cur)
print(check_code)

（2）随机生成4位字符串验证码（数字与字符都有）
import random
check_code = ''
for i in range(4):
    cur = random.randrange(0,4)    #随机猜的范围，与循环次数相等
    #字母
    if cur == i:
        tmp = chr(random.randint(65,90))    #随机取一个字母
    #数字
    else:
        tmp = random.randint(0,9)
    check_code += str(tmp)
print(check_code)
#运行结果：
#39HN










