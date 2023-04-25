import sys
import json
import socket
import time
from app.message import get_message, send_message
from app.constants import \
    ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, STATUS, RESPONSE, ERROR, IP_ADDR_DEFAULT, PORT_DEFAULT


def presence_msg(account_name='no name', status='Yep, I am here!'):
    """
    Сообщение о присутствии
    :param account_name: Значение по умолчанию 'no name'.
    :param status: Значение по умолчанию 'Yep, I am here!'.
    :return: JSON-объект
    """
    json_msg = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name,
            STATUS: status
        }
    }
    return json_msg


def check_response(message):
    """
    Проверяет ответ с сервера
    :param message: сообщение от сервера
    :return: успешное завершение или ошибка
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return f'{message[RESPONSE]}: OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def run_client():
    """
    Запускает клиентскую часть приложения, отдавая параметры командной строки '-p' и '-a'
    Пример запуска 'python client.py 192.168.1.35 8888'
    :return:
    """
    try:
        if len(sys.argv) == 1:
            addr = IP_ADDR_DEFAULT
            port = PORT_DEFAULT
        else:
            addr = sys.argv[1]
            port = int(sys.argv[2])
            if port < 1024 or port > 65535:
                raise ValueError
    except IndexError:
        print('Укажите ip-адрес и номер порта')
        sys.exit(1)
    except ValueError:
        print('Возможный порт от 1024 до 65535')
        sys.exit(1)

    # Создаём сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((addr, port))

    # Отправляем сообщение
    send_message(s, presence_msg())
    try:
        answer = check_response(get_message(s))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Используется неправильный формат JSON')


if __name__ == '__main__':
    run_client()
