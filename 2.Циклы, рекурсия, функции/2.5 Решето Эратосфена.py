"""
2.5 Решето Эратосфена
"""
import time

from func_timer import changing_number_of_semicolons

n = int(input("До какого числа получить простые числа: "))
start = time.time()
sieve = [i for i in range(n)]
sieve[1] = 0  # вычеркнул 1 (занулил 1)

for i in range(2, n):
    if sieve[i] != 0:
        j = i * 2

        while j < n:
            sieve[j] = 0
            j += i

result = [i for i in sieve if i != 0]
end = time.time()
print(result)
print(
    f'Время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')
