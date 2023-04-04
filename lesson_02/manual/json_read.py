import json

"""Чтение JSON-файлов"""


# считывает файл в JSON-формате и возвращает python-объекты
with open('msg_example_read.json') as f_n:
    objs = json.load(f_n)

for section, commands in objs.items():
    print(section, commands)

print(100 * '-')

# отвечает за считывание строки в JSON-формате и тоже возвращает python-объекты
with open('msg_example_read.json') as f_n:
    f_n_content = f_n.read()
    objs = json.loads(f_n_content)

print(objs)

for section, commands in objs.items():
    print(section)
    print(commands)
