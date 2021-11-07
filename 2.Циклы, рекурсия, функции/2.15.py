"""
Посчитать, сколько раз встречается определенная цифра в
введенной последовательности чисел. Количество вводимых
чисел и цифра, которую необходимо посчитать, задаются
вводом с клавиатуры.
Пример:
4
8
15469
5648
165489
6161
"""

numbers = int(input("Количесво чисел: "))
figure = int(input("Цифра: "))
list_ = [int(input(f"- введите {numbers - i} число: ")) for i in range(numbers)]
h = 0
for i in list_:
    for j in str(i):
        if j == str(figure):
            h += 1

print(f'Цифра: {figure}, встречается {h} раз')

# вариант 1
num = int(input("Введите количество чисел: "))
digit = int(input('Какую цифру подсчитать: '))
count = 0
for i in range(1, num + 1):
    m = int(input(f"Введите число {i}: "))
    while m > 0:
        if m % 10 == digit:
            count += 1
        m = m // 10

print(f'Было введено {count} цифр {digit}')

# вариант 2
num = int(input('Введите количесво чисел: '))
digit = input('Какую цифру подсчитать: ')
count = 0
for i in range(1, num + 1):
    ans = input(f'Введите число {i}: ')
    count += ans.count(digit)

print(f'Было введено {count} цифр {digit}')