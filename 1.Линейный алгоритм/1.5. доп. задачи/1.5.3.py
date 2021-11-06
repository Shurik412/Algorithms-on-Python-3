"""
Написать программу, которая генерирует в указанном пользователем диапазоне:
а. случайное целое число
b. случайное вещественное число
с. слуайный символ

Для каждого из трёх случаев пользователь задает свои границы
диапазона. Если надо получить случайный символ от "a" до "f",
вводятся эти символы. Программа должна вывести на экран любой символ
алфавита от 'a' до 'f' включительно.
"""
import random

num_start = input("Начало диапазона: ")
num_end = input("Конец диапазона: ")

choice = input("Ввудите номер действия:\n1.Случайное целое число\n"
               "2.Случайное вещественное число\n3.Случайный символ\n")

if choice == '1':
    print("Случайное целое число")
    num_start = int(num_start)
    num_end = int(num_end)
    result = random.randint(num_start, num_end)

elif choice == '2':
    print("Случайное вещественное число")
    num_start = float(num_start)
    num_end = float(num_end)
    result = random.uniform(num_start, num_end)

elif choice == '3':
    print("Случайный символ")
    num_start = ord(num_start)
    num_end = ord(num_end)
    result = chr(random.randint(num_start, num_end))

else:
    result = "Неизвестное действие"

print(result)
