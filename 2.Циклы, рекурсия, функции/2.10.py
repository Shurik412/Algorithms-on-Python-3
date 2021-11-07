"""
Найдите сумму n элементов следующего ряда чисел:
1, -0,5, 0,25, -0,125, ...
Количество элементов (n) вводятся с клавиатуры
"""
n = int(input("Введите число количество элементов: "))

list_ = []
start_num = 1
for _ in range(n - 1):
    list_.append(start_num)
    start_num = start_num / 2
    if start_num > 0:
        start_num = start_num * (-1)
    else:
        start_num = start_num * (-1)


print(list_)

############### ???????
n = int(input("Сколько элементов сложить: "))
item = 1
summa = 0
for i in range(n):
    print(summa)
    summa += item
    item /= -2
print(summa)
