# import logging
#
# logging.basicConfig(level=logging.INFO)
#
# logging.info('info')
# logging.critical('critical')


# import logging
#
# logging.basicConfig(
#     filename="app.log",
#     format="%(levelname)-10s %(asctime)s %(message)s",
#     level=logging.INFO
# )
#
# log = logging.getLogger('app.' + __name__)
#
# log.info('Hello, World!')
# log.warning('It seems to be a bug...')
# log.critical('Critical bug in app! Hello, World!')
#
# # Записать сообщение, используя словарь значений
# parms = {'host': 'www.python.org',
#          'port': 80
#          }
#
# log.critical("Can't connect to %(host)s at port %(port)d", parms)

import logging
import sys

# Создать регистратор верхнего уровня с именем 'app'
app_log = logging.getLogger('app')
app_log.setLevel(logging.INFO)
app_log.propagate = False

# Добавить несколько обработчиков в регистратор 'app'
app_log.addHandler(logging.FileHandler('app.log'))
app_log.addHandler(logging.StreamHandler(sys.stderr))

# Отправить несколько сообщений. Они попадут в файл app.log
# и будут выведены в поток sys.stderr
app_log.critical('Creeping death detected!')
app_log.info('FYI')
