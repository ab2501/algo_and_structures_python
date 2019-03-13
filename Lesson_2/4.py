"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите количество элементов n = '))
numbers = [1]
sum = 0

for x in numbers:
    if len(numbers) < n:
        x = (x / 2) * -1
        numbers.append(x)
for b in numbers:
    sum = sum + b
print(numbers)
print(f'Сумма из {n} элементов равна {sum}.')