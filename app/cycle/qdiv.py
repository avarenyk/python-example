def qdiv(a: int) -> int:
    q = 0
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')
    if a == 1 or a == 0:
        return '1'
    if a < 0:
        a = -a
    for i in range(1, a+1):
        if a % i == 0:
            q += 1
    return q
