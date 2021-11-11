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
