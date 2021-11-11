"""
Задача 1

В диапазоне натуральных чисел от 2 до 99 определить, сколько
из них кратны любому из чисел в диапазоне от 2 до 9.

Коментарий: количество ответов равно 8
"""

start = 2
finished = 99
natural_number = [value for value in range(2, 100)]
multiples_of_numbers = [value for value in range(2, 10)]

len_multiples_of_numbers = len(multiples_of_numbers)
len_natural_number = len(natural_number)


for divisible in natural_number:
    for divisor in multiples_of_numbers:
        result = divisible % divisor
        if result == 0:
            print(f'divisible = {divisible}, divisor = {divisor}')
