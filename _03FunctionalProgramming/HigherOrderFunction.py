# 高阶函数，就是一个函数可以接受一个函数作为参数
def func(a, b, f):
    return f(a) + f(b)


print(func(-10, 10, abs))
