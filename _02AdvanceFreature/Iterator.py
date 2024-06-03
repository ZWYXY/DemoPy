# 关于迭代
from collections.abc import Iterable

l = list(range(20))

for e in l:
    print(e)

d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

s = "abc"
for c in s:
    print(c)

## 判断一个对象是否可以迭代
a = 123
print(isinstance(a, Iterable))
print(isinstance(l, Iterable))
print(isinstance(d, Iterable))
print(isinstance(s, Iterable))

## 同时获取索引下表和内容，使用 enumerate()函数，将list变成 索引-元素对
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

## for循环同时引用两个变量
for b1, a1 in [(1, 2), (3, 4)]:
    print(a1, b1)


## 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def getMaxMin(tl):
    if not tl:  # if tl == [] || if len(tl) == 0
        return (None, None)
    max = tl[0]
    min = tl[0]
    for e in tl:
        if e > max:
            max = e
            continue
        if e < min:
            min = e
    return (min, max)


tl = list(range(100))
print(getMaxMin([7]))
