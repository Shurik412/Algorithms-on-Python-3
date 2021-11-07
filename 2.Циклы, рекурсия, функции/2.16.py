"""
Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это чисел и
сумму его цифр.
"""

# numbers = int(input("Количесво чисел: "))
# list_ = [int(input(f"- введите {numbers - i} число: ")) for i in range(numbers)]
#
# list_2 = []
# g = 0
# for i in list_:
#     for j in str(i):
#         j = int(j)
#         g += j
#
#     if g > 0:
#
#     list_2.append(g)
#     g = 0

# print(max(list_2))

##########
num = int(input('Введите натуральное число. Ноль - выйти  '))
max_sum = 0
max_num = 0
while num != 0:
    temp_num = num
    temp_sum = 0
    while num > 0:
        temp_sum += num % 10
        num //= 10
    if temp_sum > max_sum:
        max_sum = temp_sum
        max_num = temp_num
    num = int(input('Введите натуральное чисел. Ноль - выйти   '))
print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}')