"""
Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
"""

num = int(input("Номер буквы в алфавите (1-26): "))

# print(ord('a'))
# print(num)
# print(ord('a') + num)
# print(ord('a') + num - 1)
# print(chr((ord('a') + num)))
# print(chr((ord('a') + num - 1)))

num = ord('a') + num - 1

print(f"Это буква {chr(num)}")
