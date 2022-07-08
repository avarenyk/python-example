def even(a: int, b: int) -> int:
    num = []
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')
    if not isinstance(b, int):
        raise TypeError(f'Argument "b" must be integer, not {type(b)}')
    if a > b:
        a, b = b, a
    for i in range(a+1, b):
        if i % 2 == 0:
            num.append(str(i))
    return ", " . join(num)
