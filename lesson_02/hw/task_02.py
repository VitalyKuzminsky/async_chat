"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    """
    Автоматическое заполнение списка заказов.
    Принимает 5 параметров нового заказа и записывает их в JSON-файл.
    :param item: товар
    :param quantity: количество
    :param price: цена
    :param buyer: покупатель
    :param date: дата
    :return:
    """

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_write:
        orders_list = data['orders']
        new_order = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(new_order)
        json.dump(data, f_write, indent=4)


write_order_to_json('Товар 1', 1, 1000, 'Иванов', '04.04.2023')
write_order_to_json('Quantity 2', 2, 2000, 'Sidorov', '05.04.2023')
write_order_to_json('товар 3', 3, 3000, 'Кузнецов', '06.04.2023')

# Проверка файла:
with open('orders.json') as f_n:
    f_n_content = f_n.read()
    objs = json.loads(f_n_content)

print(objs)
