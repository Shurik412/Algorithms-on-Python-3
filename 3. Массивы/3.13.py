"""
Задача 8

Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
Коментарий: будет отлично если сумма будет расчитываться сразу после ввода зачений.
"""
import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(3)]
print(matrix)
# красивый (читабельный) вид матрицы
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
print()
print()

list_ = [0 for x in matrix[0]]
for index, i in enumerate(matrix):
    for index_2, j in enumerate(matrix[index]):
        if index > 0:
            val = matrix[index][index_2]
            print([x + val for x in list_])
        else:
            list_.append(j)
print(list_)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
