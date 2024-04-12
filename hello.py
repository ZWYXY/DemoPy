name = input('please input your name:')
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
