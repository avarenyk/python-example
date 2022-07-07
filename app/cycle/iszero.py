def iszero(*lst) -> int:
    for i in lst:
        if not isinstance(i, int):
            raise TypeError(f'Argument in list must be integer, not {type(i)}')
        if i == 0:
            return 'Yes'
    else:
        return 'No'
