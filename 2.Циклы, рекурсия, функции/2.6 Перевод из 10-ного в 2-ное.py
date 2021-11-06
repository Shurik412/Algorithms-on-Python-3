"""
Функция перевода десятичного числа в двоичный формате
"""
from func_timer import time_this


@time_this
def binary(num):
    s = ''
    while num > 0:
        s = str(num % 2) + str(s)
        num //= 2
    return s


# list_ = [i for i in range(256)]
# for i in list_:
#     print(f'{i}. {binary(num=i)}')

while True:
    n = int(input('Введите целое число: '))
    if n != 0:
        print(binary(n))
    else:
        break
