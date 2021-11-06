"""
Функция Аккермана
"""
import sys
import time


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


# Увеличение стека вызова функции
sys.setrecursionlimit(300000)


def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


start = time.time()
print(akk(4, 8))
end = time.time()
print(
    f'Название функции: {akk.__name__}, время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')
