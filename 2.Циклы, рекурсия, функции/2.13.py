# -*- coding: utf-8 -*-
"""
Вывести на экран коды и символы таблицы ASCII, начиная с
символа под номером 32 и заканчивая 127-м включитльено.
Вывод выполнить в табличной форме: по десять пар "код-символ"
в каждой стеке
"""
list_ = [f'{i} - {chr(i)}' for i in range(32, 128)]
remove_list = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
list_2 = remove_list(list_, 10)

for index, i in enumerate(list_2):
    st = ''
    for j in list_2[index]:
        st = st + f'| {j} |'
    print(st)

