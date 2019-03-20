"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import cProfile

def erat():
    N = 20
    def srch(c, e):
        m = N // 2
        i = 0
        j = N - 1
        while c[m] != e and i <= j:
            if e > c[m]:
                i = m + 1
            else:
                j = m - 1
            m = (i + j) // 2
        if i > j:
            return 0
        else:
            return m + 1


    from random import random
    p = 1
    q = 4
    a = [0] * N
    for i in range(N):
        a[i] = int(random() * (q - p)) + p
        p += 3
        q += 3
        print(a[i], end=' ')
    print()
    e = int(input('Число: '))
    i = srch(a, e)
    if i == 0:
        print('Такого числа нет.')
    else:
        print(f'Число находится на {i}-м месте.')


def marat():
    import random
    a = []
    for i in range(20):
        c = random.randrange(100)
        a.append(c)
        print(c, end=" ")
    print()
    b = int(input("Число: "))
    g = 1
    for i in a:
        if i == b:
            print("Число находится на {}-м месте." .format(g))
        else:
            g += 1

def main():
    marat()
    erat()

cProfile.run("main()")
