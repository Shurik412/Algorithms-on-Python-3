"""
Задача 5

В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Коментарий: При решении учесть что мы ищем сначало отрицательный а потом максимальный.
Решить без max и min
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

Выполнил!
"""
import random

array = [random.randint(-100, 100) for _ in range(10)]

print(array)
list_negative_values = []
for index, i in enumerate(array):
    if i < 0:
        list_negative_values.append(i)

print(list_negative_values)
conter = 0
for index, j in enumerate(list_negative_values):
    if index == 0:
        conter = j
    elif conter < j:
        conter = j

print(conter)

print('=' * 30)

# вариант 1
i = 0
index = -1

while i < 10:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i

    i += 1
print(f'Число {array[index]} на позиции {index}')

# вариант 2
num = float('-inf')
index = -1
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i
print(f'Число {num} на позиции {index}')
