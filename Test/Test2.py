for i in range(100):
    print(i)

i = 0
while True:
    print(i)
    i = i + 1
    if i == 10:
        break


def useKeyWord(name, age, **pets):
    print('name:', name, "age:", age, 'pets:', pets)
useKeyWord('Whos', '18', Dog='旺仔', Cat='琳娜')

def useKeyWord1(name, age, *, Dog, Cat):
    print('name:', name, "age:", age, 'pets:', Dog, Cat)
# useKeyWord1('Whos', '18', Dog='旺仔', Cat='琳娜')
useKeyWord1('Whos', '18', '旺仔', '琳娜')