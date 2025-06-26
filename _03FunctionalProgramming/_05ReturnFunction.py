from colorama import Fore, Back, Style, init
# 返回一个函数

## 在函数中定义了一个函数，把他作为函数lazy_function的返回值
def lazy_function(*args):
    a = 1
    def sums():
        ax = 0
        for n in args:
            ax += n
        return ax * a
    return sums

## 这里调用返回的是sums函数
print(lazy_function(1, 2, 3))
f = lazy_function(1, 2, 3)
print(f) ## 返回sums
print(f()) ## 返回sums函数的调用结果
print(lazy_function(1,2,3,4)())
## 观察lazy_function发现它内部的sums引用了它的入参和局部变量，
## 当lazy_sum返回函数sums时，相关参数和变量都保存在返回的函数中
## 这种称为闭包(Closure)

## 闭包的一个坑
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
## 我们觉得 f是三个不同的f(),每次装进去的i都不一样，也就是i存了三份，但实际上就存了一份，所以这里结果就是 9 9 9
## 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

### 解决方式，使用默认参数保存入参
def counter():
    fs = []
    for i in range(1,4):
        def count(i = i): # 使用默认参数保存入参
            return i*i
        fs.append(count)
    return fs
f1, f2, f3 = counter()
print(f1(), f2(), f3())

## 作业 使用闭包实现一个计数器
def counter():
    count = 0
    def calc():
        nonlocal count # nonlocal声明这个变量使用的上册函数的变量
        count += 1
        return count
    return calc

f = counter()
for i in range(1,4):
   print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
print(f())

## 思考：能不能无限套娃
def layer3():
    count = 0
    def layer2():
        nonlocal count
        count += 1
        def layer1():
            nonlocal count
            count += 1
            return count
        return layer1
    return layer2
l3 = layer3()
l2 = l3()
l1 = l2()
print(Fore.LIGHTYELLOW_EX + str(l1))






