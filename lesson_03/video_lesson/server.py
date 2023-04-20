# Программа сервера времени
from socket import *
import time


# def main():
#     """Получает запрос на соединение и отправляет клиенту текущее время"""
#     s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
#     s.bind(('', 8888))  # Присваивает порт 8888
#     s.listen(5)  # Переходит в режим ожидания запросов;
#     # одновременно обслуживает не более
#     # 5 запросов.
#
#     while True:
#         client, addr = s.accept()  # Принять запрос на соединение
#         print(f"Получен запрос на соединение от клиента с адресом: {str(addr)}")
#         time_str = time.ctime(time.time()) + "\n"
#         client.send(time_str.encode('utf-8'))
#         client.close()


# def main():
#     """TCP-соединение
#     Получает от клиента сообщение, печатает его.
#     Возвращает клиенту ответ, что всё ок.
#     При получении команды закрыться, закрывает соединение у себя и у клиента,
#     отправляя ему ответ с exit"""
#     s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
#     s.bind(('localhost', 8888))  # Присваивает порт 8888
#     s.listen(5)  # Переходит в режим ожидания запросов;
#     # одновременно обслуживает не более
#     # 5 запросов.
#
#     client, addr = s.accept()  # Принять запрос на соединение
#     print(f"Получен запрос на соединение от клиента с адресом: {str(addr)}")
#
#     while True:
#         data = client.recv(100000)  # Получаем данные в 100 тыс. байт
#         decoded_data = data.decode("utf-8")
#         print(f'Было получено сообщение: {decoded_data}')
#         if decoded_data == 'close':
#             exit_msg = 'exit'
#             client.send(exit_msg.encode('utf-8'))
#             client.close()
#             return
#
#         msg = 'Ваше сообщение получено'
#         client.send(msg.encode('utf-8'))


def main():
    """UDP-соединение"""
    s = socket(AF_INET, SOCK_DGRAM)  # Создает сокет UDP
    # Доп параметры для UDP-соединения:
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Показывает, что может слушать несколько источников.
    # 1 - это стандартный параметр

    s.bind(('localhost', 10000))  # Присваивает порт 10000

    while True:
        data = s.recv(128)  # Получаем данные в 128 байт
        decoded_data = data.decode("utf-8")
        print(f'Было получено сообщение: {decoded_data}')


if __name__ == '__main__':
    # main()  # С отработкой Traceback.
    try:
        main()
    except Exception as e:
        print(e)
