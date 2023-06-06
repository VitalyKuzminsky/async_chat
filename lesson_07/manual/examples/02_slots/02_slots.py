class MyClass:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class MyChildrenClass(MyClass):
    """My Children Class"""

    __slots__ = 'z'

    def __init__(self, z, x, y):
        super().__init__(x, y)
        self.z = z


object_01 = MyClass(1, 2)
object_children_01 = MyChildrenClass(3, 4, 5)
print(object_01.y)
print(object_children_01.x, object_children_01.z)
print(object_01.__slots__)
print('=' * 100)
print(object_children_01.__slots__)
print(object_children_01.__doc__)
