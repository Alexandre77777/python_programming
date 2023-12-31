# Для работы со специфическими форматами данных Python предоставляет
# соответствующие модули. Например, для того чтобы работать с данными в формате CSV,
# необходимо подключить модуль csv.
# Пример чтения файла users.csv, содержимое которого выглядит как:
# Mike,Dow,33,456-34-12

import csv

with open('users.csv', 'r', encoding='utf-8' ) as f: # открываем файл на чтение
    reader = csv.reader(f, delimiter=',') # создаём объект, указывая в качестве разделителя запятую
    for row in reader: # читаем файл построчно
        print(row)
    # в row приходит строка в виде списка строковых данных
    # ['Mike', 'Dow', '33', '456-34-12']


with open('users.csv', 'a', newline='' ) as f: # открываем файл на дозапись
    writer = csv.writer(f, delimiter=',') # создаём объект, указывая в качестве разделителя запятую
    writer.writerow(['John', 'Smith', 25, '123-45-67']) # Дописываем строку в файл