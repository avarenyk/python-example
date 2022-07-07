def cut(a: str):
    if not isinstance(a, str):
        raise TypeError(f'Argument "a" must be string, not {type(a)}')
    return a[2], a[-2], a[0:5], a[0:-2], a[1::2] ,a[::2], a[::-1], len(a)
