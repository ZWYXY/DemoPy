# Filter 入参跟MapReduce一样，不过不满足函数中的条件的元素会被删除
def is_odd(x):
    return x % 2 == 0

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])))
