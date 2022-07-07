def sum(*lst: int) -> int:
    s = 0
    for i in lst:
        if not isinstance(i, int):
            raise TypeError(f'Argument in list must be integer, not {type(i)}')
        s += i
    return s
