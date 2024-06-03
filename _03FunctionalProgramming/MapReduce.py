# map reduce 用法

def function(x):
    return x * x

# 其实可以这么理解map，它是把前面的function应用到每一个后面传入的参数中的元素上
r = map(function, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(r))
