# 介绍一些Python常用的高级特性
## Slice 切片，从一个List中截取部分
l = [1, 2, 3, 4, 5, 6]

pl = l[0:3]   # pl = l[:3] 从0开始0可以省略
pl1 = l[-2:]  # 倒着切片
pl2 = l[-1:]  # 倒数第一个元素下标是-1

l1 = list(range(100))
pl3 = l1[:10:2]  # 前10个数每两个取一个
pl4 = l1[::5]  # 每隔5个数取一个
pl5 = l1[:]  # 原样复制一个

print(pl)
print(pl1)
print(pl2)
print(pl3)
print(pl4)
print(pl5)

# 元组 tuple也是可以切片的
t = tuple(range(100))
t1 = t[0:5]
t2 = t[:70:10]  # 0 ~ 70中能被10整除的数
print(t1)
print(t2)

# 字符串也是可以切片的
s = "0123456789"
s1 = s[0:5]
s2 = s[1:-1]
s3 = s[0:-2]
print(s1)
print(s2)
print(s3)


#  使用切片，去除字符串首尾的空格
def trim(strs):
    while strs[0:1] == " ":
        strs = strs[1:]
    while strs[-1:] == " ":
        strs = strs[:-1]
    return strs


# print(trim("*hello*"))

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
