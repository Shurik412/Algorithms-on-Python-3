"""
Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести 6843
"""

# num = input("Введите число: ")
# num_new_list = [num[i] for i in range(len(num) - 1, -1, -1)]
# num_new = "".join(num_new_list)
# print(num_new)

#################
# Вариант 1
num = int(input("Введите целое число: "))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(result)

# вариант 2
num = input("Введите целое число: ")
result = ''
for i in num:
    result = i + result
print(result)

# вариант 3
result = num[::-1]
print(result)
