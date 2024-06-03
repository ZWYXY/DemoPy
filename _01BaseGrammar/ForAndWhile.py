# About 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sums = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sums = sums + x
print(sums)

sums = 0
for x in range(101):
    sums += x
print(sums)

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
