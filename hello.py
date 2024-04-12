name = 100  # input('please input your name:')
print('Hello World!', name)

# About List
list = [1, 2, 3, 4, 5]
list.append(7)
list.insert(5, 6)
list.pop()
list.pop(0)
print(len(list))
print(list)

# About tuple the immutable List
tuple = (1, (1,))
print(tuple)
print(len(tuple))

# else if
age = 100
if age >= 100:
    print("God")
elif age > 18:
    print("adult")
else:
    print("teenager")

elist = []
etuple = ()
if elist:  # 非0数值，非空字符串，非空list等，就判断为True，否则就是False
    print(True)
else:
    print(False)

if etuple:
    print(True)
else:
    print(False)

if "s":
    print(True)

# Switch case
score = "A"
match score:
    case 'A':
        print("A")
    case 'B':
        print("B")
    case 'C':
        print("C")
    case _:  # 匹配任意值
        print("alphabet")

# runtime = 0
# while runtime < 3:
#     scoreNum = int(input("请输入成绩："))
#     match scoreNum:
#         case 99 | 100:
#             print(f"你的分数是：{99}或{100}，简直完美")
#         case x if 90 <= x < 100:
#             print("优秀")
#         case x if 80 <= x < 89:
#             print("良好")
#         case x if 60 <= x < 79:
#             print("中等")
#         case x if x < 60:
#             print("不及格")
#         case _:  # 匹配任意值
#             print("请输入0~100的整数")
#     runtime += 1

# args = ['gcc', 'hello.c', 'world.c']
args = ['clean']
# args = ['gcc']
match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

# About 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum += x
print(sum)

# x = 1
# while x:
#     print("你真的很不错，你真的真的真的很不错")
#     x = int(input("输入数字 0 ~ 100"))

x = 1
while x:
    print("你真的很不错，你真的真的真的很不错")
    x = int(input("输入数字 0 ~ 100"))
    if x > 100:
        break
    print("还没break")

x = 1
while x:
    print("你真的很不错，你真的真的真的很不错")
    x = int(input("输入数字 0 ~ 100"))
    if x > 100:
        continue
    print("还没continue")

# About dict 就是Map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d1 = {100: 'geigei', 101: 'geigei', 102: 'geigei', 103: 'geigei', 104: 'geigei', }
print(d["Michael"])
print(d1[100])

d1[105] = "只因你太美"  # 放入数据
print(d1)
print(105 in d1)

print(d1.get(105)) # 不存在就返回None 或 -1
print(d1.pop(105)) # 删除数据
print(d1.get(105)) # 不存在就返回None 或 -1

# About Set
s = set([1,2,3,4])
print(s)
s.add(5)
print(s)
s.remove(5)
print(s)

s1 = set([3, 4])
print(s1)
print(s1&s) # 求交集
print(s1|s) # 求并集