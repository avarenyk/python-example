def evenelements(*lst: int) -> int:
    num = []
    for i in lst:
        if not isinstance(i, int):
            raise TypeError(f'Argument in list must be integer, not {type(i)}')
        if i % 2 == 0:
            num.append(i)
    return num
