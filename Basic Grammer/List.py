序列类型操作符：
1.seq[ind]              
2.seq[ind1 : ind2]    （切片操作符）
3.seq * expr (重复操作符）
4.seq1 + seq2     （连接操作符）
5.obj in seq
6.obj not in seq    （成员关系操作符）


内建函数（BIF）
1.类型转换
1） list(iter)   ——> to list
2)  str(obj)    ——> to string
3)  unicode(obj) ——>to Unicode string
4)  tuple(iter) ——>to tuple

2.可操作
1) enumerate(iter)  —— 返回enumerate对象（元组）：（index,value)
2) len(seq） —— length
3) max(seq ,key = None)  —— 返回最大值
4) min(seq ,key = None)  —— 返回最小值
5）reversed(seq） —— 逆序序列，返回新的迭代器（原先的序列顺序保持不变）
6）sorted(iter,func = None, key = None, reverse = False) —— 返回一个有序的列表（新的迭代器，原序列不变）
7）sum(seq,init=0) —— 返回序列的元素和
8）ziq(seq) —— 返回相邻元素组成的元组
