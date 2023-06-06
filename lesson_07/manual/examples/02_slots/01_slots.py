class BasicClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Создадим объект нашего класса.
bc = BasicClass(13, 42)

# В обычной ситуации все атрибуты объекта хранятся во внутреннем словаре __dict__:
print(bc.__dict__)


# Строка ниже не вызовет ошибку. Атрибут z будет добавлен в уже созданный объект
bc.z = 777
print(bc.__dict__)
print('=' * 100)


class StrictClass:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


sc = StrictClass(33, 72)
sc2 = StrictClass(11, 44)
print(sc.x)
# У объекта такого класса не будет атрибута __dict__:
print(sc.__dict__)

