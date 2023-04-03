"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).
"""

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

list_of_words = [word_1, word_2, word_3, word_4]

list_of_words_in_bit = []
for el in list_of_words:
    el_b = el.encode('utf-8')
    print(f'word "{el}" is converted to: {el_b}')
    list_of_words_in_bit.append(el_b)

print(100 * '-')

for el in list_of_words_in_bit:
    el_str = el.decode('utf-8')
    print(f'from bit to string: {el_str}')
