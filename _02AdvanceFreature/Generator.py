## g保存的是Generator算法， 每次调用就计算出下一个元素的值，知道计算出最后一个元素，直到没有更多元素时，抛出StopIteration
g = (x * x for x in range(10))

## 如何获取g中的元素，ListGenerator 和 Generate 的区别在于，ListGenerator 是一次生成全部，Generate你要的时候给你算
for n in g:
    print(n)

print("------------------------------")


## 计算feibo
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(10))
print("------------------------------")


# 定义generator函数,如果一个函数使用了yield关键字就是generator函数,它的返回值是一个Generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f2 = fib2(10)
for i in f2:
    print(i)


# 生成杨辉三角的generator
def pascal_triangle():
    row = [1]
    while True:
        yield row
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]


# 使用生成器
triangle = pascal_triangle()

# 打印前10行杨辉三角
for _ in range(10):
    print(next(triangle))
