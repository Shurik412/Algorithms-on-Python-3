import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


# test_fib(fib_list)
# test_fib(fib_dict)
# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_3" "task_4_3.fib_dict(10)"
# 1000 loops, best of 5: 4.24 usec per loop
#
# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_3" "task_4_3.fib_dict(15)"
# 1000 loops, best of 5: 6.19 usec per loop
#
# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_3" "task_4_3.fib_dict(20)"
# 1000 loops, best of 5: 8.44 usec per loop

# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_3" "task_4_3.fib_dict(100)"
# 1000 loops, best of 5: 44.8 usec per loop

# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_3" "task_4_3.fib_dict(500)"
# 1000 loops, best of 5: 254 usec per loop

# cProfile.run('fib_dict(500)')
# 19/1    0.000    0.000    0.000    0.000 task_4_3.py:14(_fib_dict)
# 39/1    0.000    0.000    0.000    0.000 task_4_3.py:14(_fib_dict)
# 199/1    0.000    0.000    0.000    0.000 task_4_3.py:14(_fib_dict)
# 999/1    0.002    0.000    0.002    0.002 task_4_3.py:14(_fib_dict)


# 1000 loops, best of 5: 8.53 usec per loop (10)
# 1000 loops, best of 5: 12.5 usec per loop (20)
# 1000 loops, best of 5: 44 usec per loop (100)
# 1000 loops, best of 5: 84.3 usec per loop (200)
# 1000 loops, best of 5: 221 usec per loop (500)

cProfile.run('fib_list(500)')
# 19/1    0.000    0.000    0.000    0.000 task_4_3.py:28(_fib_list) (10)
# 39/1    0.000    0.000    0.000    0.000 task_4_3.py:28(_fib_list) (20)
# 199/1    0.000    0.000    0.000    0.000 task_4_3.py:28(_fib_list) (100)
# 399/1    0.000    0.000    0.000    0.000 task_4_3.py:28(_fib_list) (200)
# 999/1    0.001    0.000    0.001    0.001 task_4_3.py:28(_fib_list) (500)