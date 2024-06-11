## 去掉一个字符串中的空字符串
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['a', 'b', ' ', 'c'])))