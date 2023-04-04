import csv

"""Чтение данных из файла формата CSV"""

# построчный вывод
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    for row in f_n_reader:
        print(row)

print(100 * '-')

# сам итератор
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(f_n_reader)

print(100 * '-')

# полученный итератор также можно преобразовать в список
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(list(f_n_reader))

print(100 * '-')

# отделить строки с заголовками от содержимого таблицы
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    f_n_headers = next(f_n_reader)
    print('Headers: ', f_n_headers)
    f_n_row_1 = next(f_n_reader)  # отделяем ещё и первую строку
    print('Row 1: ', f_n_row_1)
    for row in f_n_reader:
        print(row)

print(100 * '-')

# Каждой строке таблицы соответствует словарь, в котором элементы представляют собой связку «ключ (название столбца):
# значение (значение столбца)»
with open('kp_data.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)

print(100 * '-')

# Содержимое отдельных столбцов - указать их ключи-названия
with open('kp_data.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row['hostname'], row['location'])
