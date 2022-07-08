def max(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')
    if not isinstance(b, int):
        raise TypeError(f'Argument "b" must be integer, not {type(b)}')
    if a > b:
        y = a
    elif a < b:
        y = b
    else:
        y = 'a equal b'
    return y
