"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
сохранение данных в файле YAML-формата. Для этого:
а. Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
также установить возможность работы с юникодом: allow_unicode = True;
c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными.
"""

import yaml

data = {
    'product': ['cheese', 'milk', 'bread'],
    'money': 100,
    'price': {
        'cheese': '5€',
        'milk': '1€',
        'bread': '0.5€'
    }
}

with open('file.yaml', 'w', encoding='utf-8') as f_write:
    yaml.dump(data, f_write, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as f_read:
    data_new = yaml.load(f_read, Loader=yaml.SafeLoader)

print(data)
print(100 * '-')
print(data_new)
print(data == data_new)
