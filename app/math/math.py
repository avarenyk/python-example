def plus(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')
    if not isinstance(b, int):
        raise TypeError(f'Argument "b" must be integer, not {type(b)}')

    return a + b


def minus(a: int, b: int) -> int:
    pass

