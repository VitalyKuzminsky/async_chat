import csv

"""Запись данных в файл формата CSV"""

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2961', 'Baikal, str'],
        ['kp2', 'Cisco', '2962', 'Novgorod, str'],
        ['kp3', 'Cisco', '2963', 'Sochi, str'],
        ['kp4', 'Cisco', '2964', 'Vladivostok, str']]

with open('kp_data_write.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write.csv') as f_n:
    print(f_n.read())

print(100 * '-')

# Считается хорошей практикой явное указание кавычек для каждого значения, даже если оно не содержит запятых.

data = [['hostname', 'vendor', 'model', 'location'],  # Модель указал, как целое число
        ['kp1', 'Cisco', 2960, 'Moscow, str'],
        ['kp2', 'Cisco', 2960, 'Novosibirsk, str'],
        ['kp3', 'Cisco', 2960, 'Kazan, str'],
        ['kp4', 'Cisco', 2960, 'Tomsk, str']]

with open('kp_data_write_2.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write_2.csv') as f_n:
    print(f_n.read())

print(100 * '-')

"""В модуле csv для итератора реализован полезный метод writerows, позволяющий не построчно
записывать данные в файл, а передать объект (например, список) с данными в качестве аргумента и
выполнить мгновенную запись сразу всех данных"""

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', 29.60, 'Moscow, str'],
        ['kp2', 'Cisco', 29.60, 'Novosibirsk, str'],
        ['kp3', 'Cisco', 29.60, 'Kazan, str'],
        ['kp4', 'Cisco', 29.60, 'Tomsk, str']]

with open('kp_data_write_3.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    f_n_writer.writerows(data)

with open('kp_data_write_3.csv') as f_n:
    print(f_n.read())

print(100 * '-')

# В качестве разделителя можно определить любой символ
with open('kp_data_delimiter.csv') as f_n:
    f_n_reader = csv.reader(f_n, delimiter='!')
    for row in f_n_reader:
        print(row)
