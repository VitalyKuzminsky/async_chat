def split(line, types=None, delimiter=None):
    """ Разбивает текстовую строку и при необходимости
    выполняет преобразование типов.
    ...
    """
    fields = line.split(delimiter)
    if types:
        fields = [ty(val) for ty, val in zip(types, fields)]
    return fields
