"""
Задача 6

В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
Коментарий: при решении данной задачи есть 2 варианта:
1. минимальный элемент находится левей максимального
2. максимальный элемент находится левей минимального

Выполнил!
"""
import random
from icecream import ic

array = [random.randint(-100000, 1000000) for _ in range(10)]
dict_ = {}

max_ = 0
min_ = 0
pos_max = 0
pos_min = 0
for pos, i in enumerate(array):
    if i > max_:
        max_ = i
        pos_max = pos
    elif i < min_:
        min_ = i
        pos_min = pos

if pos_max > pos_min:
    ic(array[(pos_min+1):pos_max])
    summa = sum(array[(pos_min+1):pos_max])
    ic(summa)
elif pos_max < pos_min:
    ic(array[(pos_max+1):pos_min])
    summa = sum(array[(pos_max+1):pos_min])
    ic(summa)


ic(array)
ic(max_)
ic(pos_max)
ic(min_)
ic(pos_min)
