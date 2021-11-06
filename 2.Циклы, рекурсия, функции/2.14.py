"""
Написать программу, доказывающую или проверяющую, что для
множества натуральных чисел выполняется равенство:
1 + 2 + ... + n = n * (n + 1) / 2
где n - любое натуральное число
"""

n = 12
formula_one = 0
formula_two = 0
for i in range(n+1):
    formula_one += i
    formula_two = int(i * (i + 1)/2)

if formula_one == formula_two:
    print(f"Доказательство выполнено: {formula_one} = {formula_two}, где n = {n}")
