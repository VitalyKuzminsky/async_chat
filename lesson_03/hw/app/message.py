import json
from .constants import MESSAGE_SIZE, ENCODING


def send_message(socket, message):
    """
    Отправляет сообщение, закодировав его.
    :param socket: сокет
    :param message: dict - сообщение
    :return:
    """

    json_msg = json.dumps(message)
    socket.send(json_msg.encode(ENCODING))


def get_message(client):
    """
    Принимает сообщение, декодируя его в словарь.
    :param client:
    :return:
    """

    encoded_msg = client.recv(MESSAGE_SIZE)
    if isinstance(encoded_msg, bytes):  # Проверяем, что пришли байты.
        response = json.loads(encoded_msg.decode(ENCODING))
        if isinstance(response, dict):  # Проверяем, что это словарь.
            return response
        raise ValueError
    raise ValueError
