"""
Задача 3

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
Коментарий: попробуйте решить без min и max

Выполнил!
"""
import random

array = [random.randint(-100, 100) for _ in range(10)]
array_ = array
array__ = array
print(array)
max_ = 0
min_ = 0
pos_max = 0
pos_min = 0
for i in array:
    if i > max_:
        max_ = i
        pos_max = array.index(i)
    elif i < min_:
        min_ = i
        pos_min = array.index(i)

print(f'Max pos = {pos_max}')
print(f'Min pos = {pos_min}')
print(f'Max before = {array[pos_max]}')
print(f'Min before = {array[pos_min]}')
array[pos_max] = min_
array[pos_min] = max_
print(f'Max after = {array[pos_max]}')
print(f'Min after = {array[pos_min]}')
print(array)
print('=' * 20)
# вариант 1
idx_min = 0
idx_max = 0

for i in range(10):
    if array_[i] < array_[idx_min]:
        idx_min = i
    elif array_[i] > array_[idx_max]:
        idx_max = i

print(f'Min = {array_[idx_min]} в ячейке {idx_min}'
      f'\nMax = {array_[idx_max]} в ячейке {idx_max}')

array_[idx_min] = array_[idx_max]
array_[idx_max] = array_[idx_min]
print(array_)

print('=' * 20)
# Вариант 2
min_num = min(array__)
max_num = max(array__)

array__[idx_min] = array__[idx_max]
array__[idx_max] = array__[idx_min]

print(f'Min = {array__[idx_min]} в ячейке {idx_min}'
      f'\nMax = {array__[idx_max]} в ячейке {idx_max}')
array__[idx_min] = array__[idx_max]
array__[idx_max] = array__[idx_min]
print(array__)