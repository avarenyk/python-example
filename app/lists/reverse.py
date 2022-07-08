def reverse(*lst: int) -> int:
    for i in lst:
        if not isinstance(i, int):
            raise TypeError(f'Argument in list must be integer, not {type(i)}')
    return lst[::-1]
