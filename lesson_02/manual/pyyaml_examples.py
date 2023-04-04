import yaml
from yaml.loader import SafeLoader

"""Считывание данных"""

with open('data_read.yaml') as f_n:
    f_n_content = yaml.load(f_n, Loader=SafeLoader)

print(f_n_content)

print(100 * '-')

"""Запись данных"""
# запись Python-объектов (словарей с элементами-списками) в файл формата YAML
action_list = [
    'msg_1', 'msg_2', 'msg_3'
]

to_list = [
    'account_1',
    'account_2',
    'account_3'
]

data_to_yaml = {'action': action_list, 'to': to_list}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=True)

with open('data_write.yaml') as f_n:
    print(f_n.read())

print(100 * '-')

with open('data_write.yaml') as f_n:
    f_n_content = yaml.load(f_n, Loader=SafeLoader)

print(f_n_content)

