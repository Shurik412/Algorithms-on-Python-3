"""
Матрица - математический объект, записываемый в виде прямоугольной таблицы элементов.
Представляет собой совокупность строк и столбцов, на пересечении которых находятся её элементы.
Матрица в Python - список (list) вложенные во внешний список. [[1,2,3],[4,5,6],[7,8,9]]
"""
import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
print(matrix)
# красивый (читабельный) вид матрицы
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

"""
Посчитать сумму строк и столбцов матрицы
"""
print('########################################')
print('Посчитать сумму строк и столбцов матрицы')
sum_column = [0] * len(matrix[0])
print(sum_column)
print('')
for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item

        print(f'{item:>5}', end='')

    print(f'   | {sum_line}')

print('-' * (len(matrix) * 5))

for s in sum_column:
    print(f'{s:>5}', end='')

"""
Обмен значений глваной и побочной диагоналей квадратной матрицы
"""

print('\n\n################################################')
print('Обмен значений глваной и побочной диагоналей квадратной матрицы')

size = 5
matrix_ = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

for line in matrix_:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print('*' * 30)
for i in range(size):
    for j in range(size):
        if i == j:
            spam = matrix_[i][j]
            matrix_[i][j] = matrix_[i][size - 1 - j]
            matrix_[i][size-1-j] = spam

for line in matrix_:
    for item in line:
        print(f'{item:>4}', end='')
    print()
