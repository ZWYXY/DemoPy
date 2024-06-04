# About List
list = [1, 2, 3, 4, '5']
list.append(7) # 队尾追加元素
list.insert(5, 6) # 指定位置增加元素
list.pop() # 删除队尾元素
list.pop(0) # 删除指定位置元素
print(len(list))
print(list)


# About tuple the immutable List
myTuple = (1, (1,))
print(myTuple)
print(len(myTuple))