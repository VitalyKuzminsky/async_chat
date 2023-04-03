"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

file_new = open("test.txt", "w")

file_new.write("""сетевое программирование\nсокет\nдекоратор""")

file_new.close()

print(file_new)

print(100 * '-')

file = open('test.txt', 'rb')
for line in file:
    print(line.decode(encoding='utf-8'), end='')
file.close()
