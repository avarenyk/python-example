def q_words(a: str):
    if not isinstance(a, str):
        raise TypeError(f'Argument "a" must be string, not {type(a)}')
    a.replace(',', '')
    lst = a.split(' ')
    return len(lst)
