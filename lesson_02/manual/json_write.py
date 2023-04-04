import json

"""Запись в JSON-файлы"""

# dump и dumps. Первый сохраняет python-объект в json-файл. Второй возвращает строку в json-формате

dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
}

with open('mes_example_write.json', 'w') as f_n:
    f_n.write(json.dumps(dict_to_json))

with open('mes_example_write.json') as f_n:
    print(f_n.read())

print(100 * '-')

# Определение дополнительных параметров методов записи
dict_to_json = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
}

# параметры sort_keys и indent позволяют выполнить сортировку данных при записи, а также установить величину отступа
with open('mes_example_write_3.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, sort_keys=True, indent=4)

with open('mes_example_write_3.json') as f_n:
    print(f_n.read())
