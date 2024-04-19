# 函数调用
import math

pomte = print(input("请输入一些东西....\n"))


# 定义函数
def myFunc(a, b):
    return a + b
## 调用函数
print(myFunc(1, 2))

## 没想好函数体，先使用pass通过编译
def myFunc1():
    pass

## 返回一个函数
def myfunc2(a, b):
    if not isinstance(a, (int, float)):
        return TypeError("入参错误")
    if not isinstance(b, (int, float)):
        return TypeError("入参错误")
    return myFunc(a, b)

## 返回多个返回值，其实是返回了一个tuple
def move(x, y, step, angle=0):  # angle默认值是0,
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  # 看起来返回了多个值，

## 函数默认值
def register(name, pwd, nickname='新用户123', city="上海"):
    print(name)
    print(pwd)
    print(nickname)
    print(city)

register("good", "123")
register("good", "123", city="北京")  # 不按顺序调用

## 定义带可变参数的函数，可以直接传入定义好的list或tuple
def calc(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(calc(1, 2, 3, 4, 5))  # 调用可变参数
nums = [1, 2, 3, 4, 5]
print(calc(*nums))  # 已有list或者元组调用可变参数


## 关键字参数
def person(name, age, **kw):  ## 可以传入任意参数名的参数，函数使用dict接收
    print("name", name, "age", age, "other", kw)

person("你好", 12, hobby1="sing", hobby2="dance")
## 同list，可以直接传入dict
d = {"hobby":["sing","dance","rap","basketball"],"signature work":"姬霓太美"}
person("菜虚坤",18, **d)

### 关键字参数一个特殊情况，使用*隔离位置参数 和 关键字参数（这些关键字参数被命名了，所以叫命名关键字参数），位置参数只能在关键字函数之前
def person1(name, age, *, city, job) :
    print(name, age, city, job)
person1("caixukun",18, city= "sh", job="eng")

#### 特殊情况的特殊情况，如果关键字参数之前，有可变参数，可以不用再加*
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)
person2("caixukun",18, "person2", 100, city= "sh", job="eng")

## Recursion 递归，计算阶乘
### 非尾递归
def myRecursion1(n):
    if n == 1:
        return 1
    else:
        return n * myRecursion1(n-1)
print(myRecursion1(5))

print("-------------------------")

### 尾递归
def myRecursion(n, acc = 1) :
    if n == 0:
        return acc
    else :
        return myRecursion(n - 1, n * acc)

print(myRecursion(5))















