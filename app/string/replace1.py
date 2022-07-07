def replace1(a: str):
    a.lower()
    if not isinstance(a, str):
        raise TypeError(f'Argument "a" must be string, not {type(a)}')
    for i in a:
        if i == '1':
           q = a.replace('1','one')
    return q
