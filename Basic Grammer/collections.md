# collections  —— 容器数据类型

## Counter对象
**提供计数器工具以支持方便和快速的计数**
```
>>> # Tally occurrences of words in a list
>>> cnt = Counter()
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
...     cnt[word] += 1
>>> cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

>>> # Find the ten most common words in Hamlet
>>> import re
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
```

- **elements()**
**返回一个迭代器，重复每个重复次数的元素。元素以任意顺序返回。如果元素的计数小于1，elements()则忽略它**
```
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']
```

- **most_conmon([n])**
**返回n个最常见元素及其计数的列表，从最常见到最少。如果省略nNone，则 most_common()返回计数器中的所有元素。具有相同计数的元素是任意排序**
```
>>> Counter('abracadabra').most_common(3)  # doctest: +SKIP
[('a', 5), ('r', 2), ('b', 2)]
```

- **subtract()**
**从迭代或从另一个映射 （或计数器）中减去元素。喜欢dict.update()但是减去计数而不是替换它们。输入和输出都可以为零或负数。**
```
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```
