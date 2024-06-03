# Python 一些笔记
## Python数据类型
1. 字符串
2. None
3. 整数
4. 浮点数
5. 布尔类型(True | False)
## Python函数参数类型
1. 必选参数(位置参数)
2. 默认参数(def f1(a, b=1))
3. 可变参数(*args)
4. 关键字参数()
```python
def useKeyWord(name, age, **pets):
    print('name:', name, "age:", age, 'pets:', pets)
useKeyWord('Whos', '18', Dog='旺仔', Cat='琳娜')
```
5. 命名关键字函数
> 就是为了限定关键字函数的名称
```python
def useKeyWord(name, age, *, Dog, Cat):
    print('name:', name, "age:", age, 'pets:', Dog, Cat)
useKeyWord('Whos', '18', Dog='旺仔', Cat='琳娜')
```
## 函数
命名函数时，参数定义顺序 必选、默认、可变、命名关键字、关键字参数 比如：
```python
def f1(a, b, c=0, *args, **kw): # 分别是 a,b必选 c默认 *args可变 **kw 关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw): # 分别是 a,b必选 c默认 *,d命名关键字 **kw关键字
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。