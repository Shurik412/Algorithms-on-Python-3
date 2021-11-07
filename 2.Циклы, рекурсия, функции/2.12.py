"""
Написать программу, где генерируется случайное целое число
от 0 до 100. Пользователь должен его отгадать максимум за 10 попыток.
После каждой неудачи должно сообщаться, больше или меньше загаданного
то число, что ввел пользователь.
Если за 10 попыток число не отгадано - вывести его.
"""
import random

from win32comext.shell.test.testShellFolder import num

hidden_number = random.randint(0, 100)

for i in range(1, 11):
    number = int(input(f'Попытка № {i} - Введите число: '))
    if number == hidden_number:
        print("Число угадано!")
        print(f"{number} = {hidden_number}")
        break
    elif number > hidden_number:
        print("Введенное число больше загаданного! '>'")
    else:
        print("Введенное число меньше загаданного! '<'")
    if i == 10:
        print("Число не угадано!")
        print(f"Загаданное число: {hidden_number}")

##################
hidden_number = random.randint(0, 100)
print("Отгадайте число от 0 до 100 за 10 попыток")
for i in range(1, 11):
    answer = int(input(f'Попытка {i}: '))
    if num < answer:
        print("Число меньше")
    elif num > answer:
        print('Число больше')
    else:
        print(f'Вы угадали с {i}-й попыток')
        break
else:
    print(f'Поражение. Было загадано {num}')
