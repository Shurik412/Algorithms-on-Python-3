"""
Задача. В log файл сервера добавляют ip - адреса, с которых пришёл запрос.
Проанализировать последние N адресов и сохранить в новый файл пары значений "ip - количесво запросов".
- исключить локальные ip: 192.168.*.*
- сохранить исходный порядок адресов.
"""
from collections import OrderedDict, defaultdict, deque

N = 3000  # количество ip адресов

with open('file.txt', 'r', encoding='utf-8') as f:
    log = deque(f, N)

print(log)

data = OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = item[:-1]
    if not ip.startswith('192.168'):
        spam[ip] += 1
        data[ip] = 1

data.update(spam)
print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
    for key, value in data.items():
        f.write(f'{key} - {value}\n')
