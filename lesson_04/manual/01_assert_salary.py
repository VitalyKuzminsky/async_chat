import datetime
from collections import namedtuple

Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate'))


def get_salary(line):
    ''' Вычисление зарплаты работника
    '''
    line = line.split()
    if line:
        data = Salary(*line)
        fio = ' '.join((data.surname, data.name))
        salary = int(data.worked) * int(data.rate)
        res = (fio, salary)
    else:
        res = ()
    return res


def test_get_salary_summ():
    """Проверка правильности вычисления зарплаты"""
    assert get_salary('Лютиков Руслан 60 1000') == ('Лютиков Руслан', 60000), 'Неверная сумма'
    print(f'{test_get_salary_summ.__doc__}: ok')


def test_get_salary_fio():
    """Проверка получения Фамилии Имени"""
    assert get_salary('Лютиков Руслан 60 1000')[0] == 'Лютиков Руслан', 'Неверное имя'
    print(f'{test_get_salary_fio.__doc__}: ok')


def test_get_salary_empty():
    """Проверка на пустые данные"""
    assert get_salary('') == (), 'Непустые данные'
    print(f'{test_get_salary_empty.__doc__}: ok')


def test_get_salary_wrong_format():
    """Проверка на неверный формат"""
    assert get_salary(' ') == (), 'Неверный формат'
    print(f'{test_get_salary_wrong_format.__doc__}: ok')


if __name__ == "__main__":
    test_get_salary_fio()
    test_get_salary_summ()
    test_get_salary_empty()
    test_get_salary_wrong_format()
