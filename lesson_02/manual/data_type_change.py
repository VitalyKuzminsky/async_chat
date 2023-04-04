import json

tuple_ex = (
    "action",
    "to",
    "from",
    "encoding",
    "message"
)

print(type(tuple_ex))


with open('tuple_ex.json', 'w') as f_n:
    json.dump(tuple_ex, f_n, sort_keys=True, indent=2)

obj = json.load(open('tuple_ex.json'))

print(type(obj))

print(100 * '-')

# Ограничения на тип данных
# При использовании формата JSON есть ограничение: в нем нельзя сохранить словарь, где в качестве ключей — кортежи
dict_to_json = {
    ('action', 'to'): 'msg',
    'from': 'account_name'
}
# Использование дополнительного параметра 'skipkeys' = True позволяет игнорировать такие ключи и избегать ошибок
with open('dict_to_json.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, skipkeys=True)

with open('dict_to_json.json') as f_n:
    f_n_content = f_n.read()
    obj = json.loads(f_n_content)

print(obj)

print(100 * '-')

# Ключами в словарях в JSON-формате могут быть только строковые величины. Если у Python-словаря
# ключи определены в виде чисел, они будут преобразованы в строковое представление
# (data_type_change.py) без ошибок

d = {5: 300, 1: 400}

d_to_json = json.dumps(d)

print(d_to_json)
