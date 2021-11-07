# -*- coding: utf-8 -*-
"""
Разложить положительные и отрицательные числа по разным массивами
"""
import random
import time


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


start = time.time()
array = [random.randint(-100000, 100000) for _ in range(100000)]
# print(array)
end = time.time()
print(
    f'Array время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.'
)

arr_below = []
arr_lager = []

start = time.time()
# вариант 1 (Лучше - так как идет по списку и раскладываем по другим списакам)
for item in array:
    if item > 0:
        arr_lager.append(item)
    elif item < 0:
        arr_below.append(item)
end = time.time()
print(
    f'Вариант 1 время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.'
)
# print('#################################')
# print(arr_below)
# print(arr_lager)
# print('#################################')

start = time.time()
# вариант 2 (!!! хуже - потому что идет сначала по списку и ищем для положительных (отрицательных),
# а потом повторно для отрицательных (положительных). Если будет очень много элементов то потратим очень много времени!
arr_below1 = [item for item in array if item < 0]
arr_lager1 = [item for item in array if item > 0]
end = time.time()
print(
    f'Вариант 2 время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.'
)
# print('#################################')
# print(arr_below1)
# print(arr_lager1)
# print('#################################')


"""
Вставка элемента в произвольное место массива
Встроенная функция insert(позиция, вствляемый элемент) -> работает быстрее чем рукописный while.   
"""

num = int(input("Введите целое число для вставки: "))
pos = int(input("На какую позицию вставить число: "))

start = time.time()

array.append(None)
i = len(array) - 1
while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1
array[pos] = num

end = time.time()
print(
    f'Вставка элемента цикл while -> '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.'
)
# встроенная функция: array.insert(pos, num)
start = time.time()

array.insert(pos, num)
array[pos] = num

end = time.time()
print(
    f'Вставка элемента встройный insert -> '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.'
)

# Вориант создания среза (тратит больше памяти, так как формирует новый список)
# работает быстрее ну не быстрее чем
start = time.time()

array_new = array[:pos] + [num] + array[pos:]
array[pos] = num

end = time.time()
print(
    f'Вставка элемента с помощью среза  array_new = array[:pos] + [num] + array[pos:] -> '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.'
)
# print(array)
