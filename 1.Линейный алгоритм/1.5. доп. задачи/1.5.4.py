"""
Пользовать вводит две буквы.
Определить их порядковый номер в алфавите и рассчитать число букв между ними.
"""
first = input('1-я буква: ')
second = input('2-я буква: ')

print(ord(first))
print(ord(second))

first = ord(first) - ord("a") + 1
second = ord(second) - ord("a") + 1

print(f'Порядковый номер 1-й буквы = {first}, 2-й = {second}')
print(f'Число букв между введёнными: {abs(first - second) - 1}')
