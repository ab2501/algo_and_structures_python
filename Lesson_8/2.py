"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

def subs_count(array):

    count = set()
    lenght = len(array)
    for i in range(lenght):
        for j in range(i + 1, lenght + 1):
            count.add(hash(array[i:j]))

    return len(count - {hash(array)})


array = 'papa'
print(f' в строке "{array}" {subs_count(array)} подстрок')