def horse(a: str, b: int, c: str, d: int) -> str:
    if not isinstance(a, str):
        raise TypeError(f'Argument "a" must be string, not {type(a)}')
    if not isinstance(b, int):
        raise TypeError(f'Argument "b" must be integer, not {type(b)}')
    if not isinstance(c, str):
        raise TypeError(f'Argument "c" must be string, not {type(a)}')
    if not isinstance(d, int):
        raise TypeError(f'Argument "d" must be integer, not {type(b)}')
    if (a > 'h' or a < 'a') or (c > 'h' or c < 'a'):
        raise ValueError(f'{a} or/and {c} has wrong value')
    if b > 8 or d > 8 or b < 0 or d < 0:
        raise ValueError(f'{b} or/and {d} has wrong value')
    if a == c and b == d:
        raise ValueError(f'Shapes cannot be in the same cell')
    dx = abs(ord(a) - ord(c))
    dy = abs(b-d)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        return 'Yes'
    else:
        return 'No'
