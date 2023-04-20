# Программа клиента, запрашивающего текущее время
from socket import *


# def main():
#     """Создаёт соединение с сервером. Получает информацию о текущем времени,
#     которую выводи на печать"""
#     s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
#     s.connect(('localhost', 8888))  # Соединиться с сервером
#     tm = s.recv(1024)
#     s.close()
#     print(f'Time now: {tm.decode("utf-8")}')


# def main():
#     """TCP-соединение"""
#     s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
#     s.connect(('localhost', 8888))  # Соединиться с сервером
#
#     while True:
#         msg = str(input('Введите сообщение сервер: '))
#         msg_encoded = msg.encode('utf-8')
#         s.send(msg_encoded)
#         data = s.recv(1024)  # Принять не более 1024 байтов данных
#         decoded_data = data.decode('utf-8')
#         print(f"Сообщение от сервера: {decoded_data}")
#         if decoded_data == 'exit':
#             s.close()
#             return


def main():
    """UDP-соединение"""
    s = socket(AF_INET, SOCK_DGRAM)  # Создать сокет UDP
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # while True:
    #     msg = str(input('Введите сообщение сервер: '))
    #     msg_encoded = msg.encode('utf-8')
    #     s.sendto(msg_encoded, ('localhost', 10000))  # Сообщение и куда отправляем

    for i in range(1000):
        msg = f'Message - № {i}'.encode('utf-8')
        s.sendto(msg, ('localhost', 10000))  # Сообщение и куда отправляем


if __name__ == '__main__':
    # main()
    try:
        main()
    except Exception as e:
        print(e)
