# sorted用法
from operator import itemgetter

res = sorted([-100, 2, 1, 99])
print(res)
res = sorted([-100, 2, 1, 99], key=abs)
print(res)

## 小Demo
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
res = sorted(L, key=itemgetter(0))
res = sorted(L, key=itemgetter(1), reverse=True)


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


def fn(t):  # by_score一种特殊写法
    return -t[1]


res = sorted(L, key=by_name)
res = sorted(L, key=fn)
print(res)
