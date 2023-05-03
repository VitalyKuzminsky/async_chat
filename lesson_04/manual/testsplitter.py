import unittest


def split(line, types=None, delimiter=None):
    """ Разбивает текстовую строку и при необходимости
    выполняет преобразование типов.
    ...
    """
    fields = line.split(delimiter)
    if types:
        fields = [ty(val) for ty, val in zip(types, fields)]
    return fields


# Модульные тесты
class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_simple_string(self):
        r = splitter.split('GOOG 100 490.50')
        self.assertEqual(r,['GOOG','100','490.50'])

    def test_type_convert(self):
        r = splitter.split('GOOG 100 490.50', [str, int, float])
        self.assertEqual(r,['GOOG', 100, 490.5])

    def test_delimiter(self):
        r = splitter.split('GOOG,100,490.50',delimiter=',')
        self.assertEqual(r,['GOOG','100','490.50'])


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
