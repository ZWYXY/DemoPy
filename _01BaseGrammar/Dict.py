# About dict 就是Java中的Map集合
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d1 = {100: 'geigei', 101: 'geigei', 102: 'geigei', 103: 'geigei', 104: 'geigei', }
print(d["Michael"])
print(d1[100])

d1[105] = "只因你太美"  # 放入数据
print(d1)
print(105 in d1)

print(d1.get(105)) # 不存在就返回None 或 -1
print(d1.pop(105)) # 删除数据
print(d1.get(105)) # 不存在就返回None 或 -1