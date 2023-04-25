import json
import sys
import socket
from app.message import get_message, send_message
from app.constants import ACTION, ACCOUNT_NAME, RESPONSE, LISTEN, PRESENCE, TIME, USER, ERROR, PORT_DEFAULT


def check_message(message):
    """
    Проверяет запрос от клиента и возвращает ответ сервера с соответствующим кодом
    :param message: dict - сообщение от клиента
    :return: dict - ответ
    """
    if ACTION in message and message[ACTION] == \
            PRESENCE and TIME in message and USER in message and message[USER][ACCOUNT_NAME] == 'no name':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Неправильный запрос'
    }


def run_server():
    """
    Запускает сервер, принимая параметры командной строки '-p' и '-a'.
    При их отсутствии берёт значения по умолчанию.
    Пример запуска: 'python server.py -p 8888 -a 192.168.1.35'
    :return:
    """

    # Обработка порта
    try:
        if '-p' not in sys.argv:
            listen_port = PORT_DEFAULT
        else:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            if listen_port < 1024 or listen_port > 65535:
                raise ValueError
    except IndexError:
        print('Укажите номер порта')  # Параметр порта указан, но нет значения:
        sys.exit(1)
    except ValueError:
        print('Возможный порт от 1024 до 65535')  # Номер порта указан из зарезервированных значений:
        sys.exit(1)

    # Обработка ip-адреса
    try:
        if '-a' not in sys.argv:
            listen_address = ''
        else:
            listen_address = sys.argv[sys.argv.index('-a') + 1]

    except IndexError:
        print('Укажите ip-адрес, который будет слушать сервер.')  # Параметр ip-адреса указан без значения
        sys.exit(1)

    # Создаём сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((listen_address, listen_port))
    s.listen(LISTEN)

    # Получаем сообщение, проверяем, обрабатываем, отправляем, закрываем соединение.
    while True:
        client, addr = s.accept()
        try:
            msg = get_message(client)
            print(msg)
            response = check_message(msg)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Используется неправильный формат JSON')
            client.close()


if __name__ == '__main__':
    run_server()
