"""Декоратор"""
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Call {func.__name__} args: {args} kwargs{kwargs}')
#         result = func(*args, **kwargs)
#         print(f'In wrapper {func.__name__} return {result}')
#         return result
#     return wrapper
#
#
# @trace
# def square(x):
#     print('Working func square...')
#     return x*x
#
#
# square(2)
#
# print(100 * '=')

"""Декторатор через классы"""
# class Log:
#     def __int__(self) -> None:
#         pass
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(f'Call from class {func.__name__} args: {args} kwargs{kwargs}')
#             result = func(*args, **kwargs)
#             print(f'In wrapper {func.__name__} return {result}')
#             return result
#         return wrapper
#
#
# @Log()
# def square(x):
#     print('Working func square...')
#     return x*x
#
#
# square(4)


"""Несколько дектораторов"""
# def level1(func):
#     def wrapper(*args, **kwargs):
#         print(f'start deep 1')
#         result = func(*args, **kwargs)
#         print(f'stop deep 1')
#         return result
#     return wrapper
#
#
# def level2(func):
#     def wrapper(*args, **kwargs):
#         print(f'start deep 2')
#         result = func(*args, **kwargs)
#         print(f'stop deep 2')
#         return result
#     return wrapper
#
#
# def level3(func):
#     def wrapper(*args, **kwargs):
#         print(f'start deep 3')
#         result = func(*args, **kwargs)
#         print(f'stop deep 3')
#         return result
#     return wrapper
#
#
# @level1
# @level2
# @level3
# def square(x):
#     print('Working func square...')
#     return x*x
#
#
# square(4)


"""Декоратор с параметрами"""
from functools import wraps

class Log:
    """Дока к классу"""
    def __int__(self) -> None:
        pass

    def __call__(self, func):
        @wraps(func)  # Добавляет все параметры целевой функции.
        def wrapper(*args, **kwargs):
            """Дока к wrapper"""
            print(f'Call from class {func.__name__} args: {args} kwargs{kwargs}')
            result = func(*args, **kwargs)
            print(f'In wrapper {func.__name__} return {result}')
            return result

        # wrapper.__doc__ = func.__doc__  # Так можно заставить декоратор отображать документацию для декорируемой фии
        return wrapper


@Log()
def square(x):
    """ Вычисляет квадрат
    >>> square(4)
    16
    """
    print('Working func square...')
    return x*x


square(4)
print(square.__doc__)

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
