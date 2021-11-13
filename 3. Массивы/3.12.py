"""
Задача 7

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.

Выполнил
"""
import random

array = [random.randint(-100, 100) for _ in range(10)]
array_ = array
print(array_)
print(array)


def find_min():
    counter = 0
    counter_index = 0
    for index, i in enumerate(array):
        if index == 0:
            counter = i
            counter_index = index
        elif counter > i:
            counter = i
            counter_index = index
    del array[counter_index]
    result = [counter, counter_index]
    return result


find_one = find_min()
print(f'Первый минимальный элемент: {find_one[0]}')
find_two = find_min()
print(f'Второй минимальный элемент: {find_two[0]}')

print('=' * 30)
array_ = [random.randint(-100, 100) for _ in range(10)]
print(array_)
if array_[0] > array_[1]:
    min_idx_1 = 0
    min_idx_2 = 1
else:
    min_idx_1 = 1
    min_idx_2 = 0

for i in range(2, 10):
    if array_[i] < array_[min_idx_1]:
        spam = min_idx_1
        min_idx_1 = i
        if array_[spam] < array_[min_idx_2]:
            min_idx_2 = spam
    elif array_[i] < array_[min_idx_2]:
        min_idx_2 = i

print(f'Число {array_[min_idx_1]} в ячейке {min_idx_1}')
print(f'Число {array_[min_idx_2]} в ячейке {min_idx_2}')
