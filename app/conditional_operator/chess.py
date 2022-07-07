def chess(a: str, b: int, c: str, d: int) -> str:
    if not isinstance(a, str):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')
    if not isinstance(b, int):
        raise TypeError(f'Argument "b" must be string, not {type(b)}')
    if not isinstance(c, str):
        raise TypeError(f'Argument "c" must be integer, not {type(a)}')
    if not isinstance(d, int):
        raise TypeError(f'Argument "d" must be string, not {type(b)}')
    if (a or c) > 'h' or (a or c) < 'a':
        raise ValueError(f'{a} or/and {c} has wrong value') 
    if (b or d) > 8 or (b or d) < 0:
        raise ValueError(f'{b} or/and {d} has wrong value')
    if a == c and b == d:
        raise ValueError(f'Shapes cannot be in the same cell')
    if a == c or b == d:
        return 'Yes'
    else:
        return 'No'


#print(chess('a', 7, 'h', 8))