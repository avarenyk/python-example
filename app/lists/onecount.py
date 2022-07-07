def onecount(*lst: int) -> int:
    q = []
    for i in lst:
        if not isinstance(i, int):
            raise TypeError(f'Argument in list must be integer, not {type(i)}')
        if lst.count(i) == 1:
            q.append(i)
    return q
