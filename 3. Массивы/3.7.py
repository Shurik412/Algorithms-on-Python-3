"""
Задача 2

Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.

Выполнено!
"""
import random

array_one = [random.randint(-100, 100) for _ in range(10)]
print(array_one)
array_two = []
for index, i in enumerate(array_one):
    if i % 2 == 0:
        array_two.append(index)
print(array_two)

##########################################
# SIZE = 10
# array_ = [random.randint(-100, 100) for _ in range(SIZE)]
# print(array_)

result = []

for i in range(len(array_one)):
    if array_one[i] % 2 == 0:
        result.append(i)

print(f'Индексы четных элементов: {result}')