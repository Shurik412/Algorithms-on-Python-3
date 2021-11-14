from collections import Counter

a = Counter()  # пустая коллекция
b = Counter('abrakadabra')  # коллекция основанная на строке
c = Counter({'red': 2, 'blue': 4})  # коллекция основанная на словаре
d = Counter(cats=4, dogs=5)  # коллекция основанная на ключевых аргументах

print(a, b, c, d, sep='\n')
print(b['z'])
b['z'] = 0
print(b)
print(list(b.elements()))
print(b.most_common(2))

# вычитание из одной коллекции другую g.subtract(f)
g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
g.subtract(f)
print(g)

print('*' * 50)
# приведем во множество или словарь
print(set(g))
print(dict(g))
# чистка удаление всех элементов
g.clear()
print(g)

print('*' * 50)
# логические операции +, -, и, или
x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)
print(x | y)

print('*' * 50)
# Унарное сложение и вычитание
z = Counter(a=2, b=-4)
print(+z)
print(-z)
