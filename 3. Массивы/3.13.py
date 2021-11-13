"""
Задача 8

Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
Коментарий: будет отлично если сумма будет расчитываться сразу после ввода зачений.

Выполнено!
"""
import random
from icecream import ic

# matrix = [[input('Введите число: ') for _ in range(5)] for _ in range(4)]
matrix = [[random.randint(-100, 100) for _ in range(4)] for _ in range(4)]

# красивый (читабельный) вид матрицы
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print()

matrix_ = matrix
list_sum_row = []
for index_i, i in enumerate(matrix):
    counter = 0
    for index_j, j in enumerate(i):
        counter += j
    list_sum_row.append(counter)

list_sum_column = []
counter = 0
for j in range(len(matrix[0])):
    counter = 0
    for i in matrix:
        counter += i[j]
    list_sum_column.append(counter)

for index_i, i in enumerate(matrix):
    i.append('|')
    i.append(list_sum_row[index_i])

matrix.append(['-' for _ in range(len(matrix[0]))])
matrix.append(list_sum_column)

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

print('=' * 30)
M = 5
N = 4
matrix = []
for i in range(N):
    row = []
    summ = 0
    for j in range(M - 1):
        num = int(input(f'Строка {i}, элемент {j}: '))
        summ += num
        row.append(num)
    row.append(summ)
    matrix.append(row)

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()
