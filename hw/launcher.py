"""Лаунчер"""

import subprocess

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(subprocess.run(['python', 'server.py']))
        for i in range(2):
            PROCESS.append(subprocess.run(['python client.py', '-m send']))
        for i in range(5):
            PROCESS.append(subprocess.run(['python client.py', '-m listen']))
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
