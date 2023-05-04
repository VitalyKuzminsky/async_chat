import sys
import os
import logging
import logging.handlers
sys.path.append('../')

# создаём формировщик логов (formatter):
SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(logging.INFO)

# отладка
if __name__ == '__main__':
    LOGGER.info('Сообщение уровня: INFO')
    LOGGER.warning('Сообщение уровня: WARNING')
    LOGGER.error('Сообщение уровня: ERROR')
    LOGGER.critical('Сообщение уровня: CRITICAL')
