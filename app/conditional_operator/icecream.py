def icecream(a: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')
    if a <= 0:
        raise ValueError(f'Argument "a":{a} must be bigger than 1')
    if (a % 3 == 0 or a % 5 == 0) and a < 6:
        return 'Yes'
    else:
        return 'No'
print(icecream(33))