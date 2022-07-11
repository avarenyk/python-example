def sort(*lst: int) -> int:
    if not isinstance(lst[0], int):
        raise TypeError(f'Argument in list must be integer, not {type(lst[0])}')
    lst = list(lst)
    for i in range(0, len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst