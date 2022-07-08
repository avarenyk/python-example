def year(a: int) -> str:
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')
    if a <= 0:
        raise ValueError(f'Argument "a":{a} must be bigger than 1')
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return 'Yes'
    else:
        return 'No'
