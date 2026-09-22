"""Задача с чтением и анализом файла"""
from datetime import datetime

cnt_error = 0
cnt_warning = 0
cnt_info = 0

dates = []
# этот код убирает все устые строки
with (open(r'/Users/kseniaperesada/Desktop/untitled folder/log.txt', encoding='utf-8') as f):
    for line in f:
        line = line.strip()
        if not line:
            continue # if not line: — если line пустая (''), то условие истинно (потому что пустая строка в Python считается ложной).

        parts = line.split()
        level = parts[1]
        dates.append(datetime.strptime(parts[0], '%Y-%m-%d'))
        if level =='ERROR':
            cnt_error += 1
        elif level =='WARNING':
            cnt_warning += 1
        elif level =='INFO':
            cnt_info += 1
        # parts[0] — дата, parts[1] — уровень, parts[2:] — текст
        print(parts)
        print(parts[1])
    print(cnt_error)
    print(cnt_warning)
    print(cnt_info)
    print(f'Количество ошибок ИНФО: {cnt_info} \nКоличество ошибок ERROR: {cnt_error} \nКоличество ошибок WARNING: {cnt_warning}')
print(max(dates))
print(min(dates))
print(max(dates)-min(dates))