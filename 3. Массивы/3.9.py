"""
Задача 4

Определить, какое число в массиве встречается чаще всего.
Коментарий: сделать диапазон в рандоме меньше чтобы элементы встречались чаще

Выполнил!
"""

import random
from icecream import ic

array = [random.randint(-10, 10) for _ in range(100)]
dict_ = {}
for i in set(array):
    counter = 0
    for j in array:
        if i == j:
            counter += 1
    dict_[i] = counter

ic(dict_)

# вариант 1
print('=' * 20)
SIZE = 10
array_ = [random.randint(0, SIZE // 1.5) for _ in range(10)]
print(array_)
num = array_[0]
max_frq = 1

for i in range(SIZE - 1):
    frq = 1
    for k in range(i + 1, SIZE):
        if array_[i] == array_[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array_[i]
if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз')
else:
    print('Все элементы уникальны')

# вариант 2
print('=' * 30)
diction = {}
for item in array:
    if item in diction.keys():
        diction[item] += 1
    else:
        diction[item] = 1

ic(diction)
