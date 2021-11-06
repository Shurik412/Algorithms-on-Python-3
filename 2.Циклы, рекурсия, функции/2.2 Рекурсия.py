"""
Рекрусия - вызов функции самой себя;

Задача: Даны два целых числа А и ВведитеНеобходимо вывести все числа от А до В
включитльено, в порядке возрастания, если А < B, или в порядке убывания, если А > B.
Максимальная глубина рекурсии 1000.
т.е. глубина стека памяти 1000.
Используйте метод рекурсии там где глубина меньше 1000
"""
import time
from func_timer import changing_number_of_semicolons


def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'


start = time.time()
print(func(1, 10000))
end = time.time()
print(
    f'Название функции: {func.__name__}, время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')
