# import logging
# import sys
#
# # Определить формат сообщений
# _format = logging.Formatter("%(levelname)-10s %(asctime)s %(message)s")
#
# # Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
# crit_hand = logging.StreamHandler(sys.stderr)
# crit_hand.setLevel(logging.CRITICAL)
# crit_hand.setFormatter(_format)
#
# # Создать регистратор
# log = logging.getLogger('basic')
# # Добавить обработчик к регистратору
# log.addHandler(crit_hand)
# # Передать сообщение обработчику
# log.critical('Oghr! Kernel panic!')

import logging
import sys

# Определить формат сообщений
format = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

# Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(format)

# Создать обработчик, который выводит сообщения в файл
applog_hand = logging.FileHandler('app.log')
applog_hand.setFormatter(format)

# Создать регистратор верхнего уровня с именем 'app'
app_log = logging.getLogger('app')
app_log.setLevel(logging.INFO)
app_log.addHandler(applog_hand)
app_log.addHandler(crit_hand)

# Изменить уровень важности для регистратора 'app.net'
logging.getLogger('app.net').setLevel(logging.ERROR)
