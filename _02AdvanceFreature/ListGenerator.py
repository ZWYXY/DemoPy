# 列表生成式
import os

print(list(range(0, 100)))
print(list(range(100)))
print([x * x for x in range(1, 11)])  # * 相当于运算符
print([x * x for x in range(1, 11) if x % 2 == 0])

## 使用双层for实现全排列
print([m + n for m in "abc" for n in "efg"])  # +相当于运算符

## 迭代当前目录下的所有目录和文件
print([d for d in os.listdir()])

## for循环同时迭代多个变量
d = {'key1': "1", 'key2': "2", 'key3': "3", 'key4': "4", "key5":"-5"}
for k, v in d.items():
    print(k, ':', v)

## 因此，列表生成式也可以使用两个变量来生成list
print([k + "=" + v for k, v in d.items()])

## 大小写转换，其实就是可以用函数
print([k.upper() + "=" + v.lower() for k, v in d.items()])

## for后使用If过滤
print([k.upper() + "=" + v.lower() for k, v in d.items() if int(v) > 2])

## for前使用if-else计算，他必须依据x算出一个结果
print([k.upper() + "=" + v.lower() if isinstance(v, str) else print("instance") for k, v in d.items()])
