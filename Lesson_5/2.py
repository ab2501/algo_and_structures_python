"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

def listing(st):
    a = []
    for i in st:
        a.append(i)
    return a
def string(st):
    a = ""
    for i in st:
        a += i
    return a
def itg(st):
    a = []
    b = 1
    for i in st:
        a.append(i)
    c = a[2:]
    return c

first = input("Введите первое 16-иричное число(прииер - d5a1): ")
second = input("Введите второе 16-иричное число(прииер - d5a1): ")
print()
first = listing(first)
second = listing(second)
print("Первое число - {}\nВторое число - {}".format(first, second))

f = int(string(first), 16)
s = int(string(second), 16)

summ = itg(hex(f + s))
op = itg(hex(f * s))

print("Сумма чисел - {}\nИх произведение - {}" .format(summ, op))