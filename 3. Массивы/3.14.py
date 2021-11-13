"""
Задача 9
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Коментарий: создайте матрицу 5х5, найдите минимальный элемент в каждом из стлобцов, а
потом среди минимальных вычисляем максимальный. (без max, min)

Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
 в том числе написанных самостоятельно.
В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
 используйте один любой по вашему выбору.

 Выполнено!
"""

import random


matrix = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]
print(matrix)
# красивый (читабельный) вид матрицы
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print()
print()

list_ = []
for index_i, i in enumerate(matrix):
    for index_j, j in enumerate(i):
        if index_i == 0:
            list_.append(matrix[index_i][index_j])
        else:
            if matrix[index_i][index_j] < list_[index_j]:
                list_[index_j] = matrix[index_i][index_j]

print(f'Минимальный среди столбцов матрицы: {list_}')

j = 0
for i in list_:
    if i < j:
        j = i

print(f'Минимальный среди минимальных: {j}')

print('=' * 30)

for line in matrix:
    print(*line, sep='\t')

max_ = matrix[0][0]
for j in range(5):
    min_ = matrix[0][j]
    for i in range(5):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]
    if min_ > max_:
        max_ = min_

print(f'Max in min = {max_}')