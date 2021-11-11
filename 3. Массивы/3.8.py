"""
Задача 3

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
Коментарий: попробуйте решить без min и max

Выполнил!
"""
import random

array = [random.randint(-2300000, 10000000) for _ in range(100)]
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
