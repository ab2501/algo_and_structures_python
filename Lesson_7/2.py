"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random
array = [round(random.uniform(0.0, 50.0), 2) for i in range(0, 10)]


def sorted_by_merge(array: list):

    def split_array(array: list):
        if len(array) <= 1:
            return array

        left = []
        right = []
        rand_index = random.randint(0, len(array) - 1)
        rand_element = array[rand_index]
        array.pop(rand_index)

        for item in array:
            if item >= rand_element:
                right.append(item)
            else:
                left.append(item)

        # print(f'--> {left} {[rand_element]} {right}')
        return split_array(left) + [rand_element] + split_array(right)
    return split_array(array)



print(f' Исходный массив:{array}')
array = sorted_by_merge(array)
print(f' Отсортированный массив:{array}')