# map reduce 用法
from functools import reduce

## map
def function(x):
    return x * x

### 其实可以这么理解map，它是把前面的function应用到每一个后面传入的参数中的元素上
r = map(function, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(r))

### 一些使用场景，将数字转变为字符
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8])))


## reduce
### 使用reduce求阶乘
def function1(x, y):
    return x * y
res = reduce(function1, [1, 2, 3, 4, 5])
print(res)

### 使用reduce 将[1, 2, 3, 4, 5]变成12345
def fn(x, y):
    return x * 10 + y
res = reduce(fn, [1, 2, 3, 4, 5])
print(res)


## 使用map + reduce 将'12345'变成12345
def str2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
res = reduce(fn, map(str2num, '12345'))
print(res)

### 简化一下
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn1(x, y):
        return 10 * x + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn1, map(char2num, s))
print(str2int("1234567"))