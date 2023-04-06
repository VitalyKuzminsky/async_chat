import re
import csv

"""1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data(), а также
сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv()."""


def get_data():
    """
    Осуществляет перебор txt файлов с данными, их открытие и считывание данных. В этой функции из считанных данных
    необходимо с помощью регулярных выражений извлечь значения параметров:
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    :return main_data: -> list Главный список для хранения данных отчета.
    """

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        # С помощью регулярных выражений извлечь значения параметров:
        search_file = open(f'info_{i}.txt')
        data = search_file.read()

        os_prod_el = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_el.findall(data)[0].split()[2])

        os_name_el = re.compile(r'Название ОС:\s\S*')
        os_name_list.append(os_name_el.findall(data)[0].split()[2])

        os_code_el = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_el.findall(data)[0].split()[2])

        os_type_el = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_el.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    j = 1
    for i in range(0, 3):
        row_data = [j, os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(row_data)
        j += 1

    return main_data


def write_to_csv(link_to_file):
    """
    Принимает ссылку на CSV-файл.
    Получает данные через вызов функцию get_data() и сохраняет их в указанный CSV-файл
    :param link_to_file: название файла
    :return:
    """

    main_data = get_data()
    with open(link_to_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            writer.writerow(row)


write_to_csv('report.csv')
