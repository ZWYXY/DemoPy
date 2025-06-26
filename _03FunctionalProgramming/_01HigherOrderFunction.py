# 高阶函数，就是一个函数可以接受一个函数作为参数
def func(a, b, my_func):
    return my_func(a) + my_func(b)


print(func(-10, 10, abs))
