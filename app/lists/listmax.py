def listmax(*lst: int) -> int:
    for i in lst:
        if not isinstance(i, int):
            raise TypeError(f'Argument in list must be integer, not {type(i)}')
    return max(lst), lst.index(max(lst))
