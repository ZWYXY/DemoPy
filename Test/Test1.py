L = [1]
M = [2]
LM = L + M + [3]
print(LM)

A = [1, 2]
P = [1] + [A[i] + A[i + 1] for i in range(3)] + [1]
print("---------------------")
print(P)
print("---------------------")


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
