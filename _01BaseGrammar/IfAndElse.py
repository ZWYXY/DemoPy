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
