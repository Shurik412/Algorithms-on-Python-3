import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# test_fib(fib)

cProfile.run('fib(10)')


# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_2" "task_4_2.fib(10)"
# 1000 loops, best of 5: 22.7 usec per loop
#
# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_2" "task_4_2.fib(15)"
# 1000 loops, best of 5: 269 usec per loop
#
# C:\01_ProjectPy\Algorithms_Python3\4_Algorithm_evaluation>python -m timeit -n 1000 -s "import task_4_2" "task_4_2.fib(20)"
# 1000 loops, best of 5: 3.05 msec per loop
