import time
from func_timer import changing_number_of_semicolons

"""
Алгоритмическое представление
цикла с предусловием
"""

num = int(input("Введите целое число: "))
while num > 0:
    print(num % 10)
    num //= 10

"""
Алгоритмическое представление
цикла с постусловием (Python - такого цикла нет (есть совместно с break))
"""
while True:
    num = float(input("Введите число от 0 до 100: "))
    if num >= 0 and num <= 100:
        break

while True:
    num = float(input("Введите число от 0 до 100: "))
    if 0 <= num <= 100:
        break

"""
Алгоритмическое представление
цикл с параметром
(арифметический цикл) (заранее известно количество итераций)
"""

i = 0
start = time.time()
while i <= 10:
    print(i)
    i += 1
end = time.time()
print(
    f'Название цикла: while, время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')


start = time.time()
for i in range(11):
    print(i)
end = time.time()
print(
    f'Название цикла: for, время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')
