import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_loop(n):
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second


# test_fib(fib_loop)

# 1000 loops, best of 5: 904 nsec per loop (10)
# 1000 loops, best of 5: 5.83 usec per loop (100)
# 1000 loops, best of 5: 6.2 usec per loop (500)
# 1000 loops, best of 5: 32.4 msec per loop (50000)

# cProfile.run('fib_loop(1000)')


# 1    0.000    0.000    0.000    0.000 task_4_4.py:11(fib_loop) (10)
# 1    0.000    0.000    0.000    0.000 task_4_4.py:11(fib_loop) (1000)

# технология Мемоизация (сохраниене результата функции и с последующем использовании
@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# 1000 loops, best of 5: 123 nsec per loop (100)

cProfile.run('fib(200)')

# 101/1    0.000    0.000    0.000    0.000 task_4_4.py:35(fib) (100)
# 201/1    0.000    0.000    0.000    0.000 task_4_4.py:35(fib) (200)
