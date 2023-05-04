import socket
import sys
import argparse
import json
import logging
import logs.server_log_config
from errors import IncorrectDataRecivedError
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, PORT_DEFAULT, LISTEN, ERROR
from common.utils import get_message, send_message

SERVER_LOGGER = logging.getLogger('server')  #Инициализация логирования сервера.


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь - сообщение от клинта,
    проверяет корректность, возвращает словарь-ответ для клиента
    :param message:
    :return:
    """
    SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and \
            USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def create_arg_parser():
    """
    Парсер аргументов коммандной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=PORT_DEFAULT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию
    :return:
    """
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    # проверка получения корректного номера порта для работы сервера.
    if not 1023 < listen_port < 65536:
        SERVER_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта '
                               f'{listen_port}. Допустимы адреса с 1024 до 65535.')
        sys.exit(1)
    SERVER_LOGGER.info(f'Запущен сервер, порт для подключений: {listen_port}, '
                       f'адрес с которого принимаются подключения: {listen_address}. '
                       f'Если адрес не указан, принимаются соединения с любых адресов.')
    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(LISTEN)

    while True:
        client, client_address = transport.accept()
        SERVER_LOGGER.info(f'Соединение установлено с клиентом: {client_address}')
        try:
            message_from_cient = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение: {message_from_cient}')
            response = process_client_message(message_from_cient)
            SERVER_LOGGER.info(f'Ответ клиенту: {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Закрывается соединение с клиентом: {client_address}')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать JSON строку от клиента {client_address}')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'Используется неправильный формат JSON от клиента {client_address}')
            client.close()


if __name__ == '__main__':
    main()
