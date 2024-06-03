# About List
list = [1, 2, 3, 4, 5]
list.append(7)
list.insert(5, 6)
list.pop()
list.pop(0)
print(len(list))
print(list)

# About Set
s = set([1,2,3,4])
print(s)
s.add(5)
print(s)
s.remove(5)
print(s)

s1 = set([3, 4])
print(s1)
print(s1&s) # 求交集
print(s1|s) # 求并集

# About tuple the immutable List
myTuple = (1, (1,))
print(myTuple)
print(len(myTuple))