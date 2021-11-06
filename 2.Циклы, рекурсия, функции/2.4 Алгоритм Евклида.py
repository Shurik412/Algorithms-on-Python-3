from func_timer import time_this
import time


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


"""
Алгоритм Евклида
"""

"""
1. Вариант. Простейший цикл алгоритм основанный 
на вычислении
(Работает очень долго)
"""

m = 540
n = 250000000


@time_this
def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


print(f'gcd = {gcd(m, n)}')

"""
2 Вариант. Рекурсивный алгоритм основанный на нахождении 
остатка от делителя
(Работает быстро. 
Использует рекурсию, есть вероятность ошибки: переполнение глубины стека,
также потребляет больше ОЗУ)
"""


def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


start = time.time()
print(f'gcd2 = {gcd2(m, n)}')
end = time.time()
print(
    f'Название функции: {gcd2.__name__}, время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')

"""
3 Вариант. Циклический алгоритм основанный на нахождении 
остатка от деления 
(Работает быстро, рекомендуется использовать)
"""


@time_this
def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(f'gcd3 = {gcd3(m, n)}')
