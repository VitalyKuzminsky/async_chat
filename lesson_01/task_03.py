"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.
"""


word_1 = 'attribute'
word_2 = 'класс'
word_3 = 'функция'
word_4 = 'type'

list_of_words = [word_1, word_2, word_3, word_4]

for el in list_of_words:
    try:
        print(f'Conversion to bit type for word ({bytes(el, "ascii")}) is done: {type(bytes(el, "ascii"))}')
    except UnicodeEncodeError:
        print(f'Conversion to bit type for word ({el}) is not possible')
