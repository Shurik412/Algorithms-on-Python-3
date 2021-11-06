# -*- coding: utf-8 -*-
import time
from functools import wraps


def changing_number_of_semicolons(number, digits=0):
    return f"{number:.{digits}f}"


def time_this(func):
    """
    Декоратор для определения веремени работы функции.
    :param func: любая функция
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f'Название функции: {func.__name__}, время работы: '
            f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')
        return result

    return wrapper


if __name__ == '__main__':

    # Testing @timethis
    @time_this
    def countdown(n):
        """

        :param n:
        :return:
        """
        while n > 0:
            # print(n)
            n = n - 1


    countdown(1000000)
