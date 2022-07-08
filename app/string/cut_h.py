def cut_h(a: str):
    a.lower()
    q = []
    if not isinstance(a, str):
        raise TypeError(f'Argument "a" must be string, not {type(a)}')
    for i in range(len(a)):
        if a[i] == 'h':
            q.append(i)
    return a.replace(a[q[0]:(q[-1])+1], '')
