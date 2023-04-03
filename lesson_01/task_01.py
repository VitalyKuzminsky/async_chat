"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'

list_of_words = [word_1, word_2, word_3]

for el in list_of_words:
    print(f'type: {type(el)}, element: {el}')

print(100 * '-')

word_unicode_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_unicode_2 = '\u0441\u043e\u043a\u0435\u0442'
word_unicode_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

list_of_words_unicode = [word_unicode_1, word_unicode_2, word_unicode_3]

for el in list_of_words_unicode:
    print(f'type: {type(el)}, element: {el}')
