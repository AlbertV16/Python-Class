def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invert = {}
    for i in d:
        if d[i] in invert:
            invert[d[i]].extend([i])
            invert[d[i]].sort()
        else:
            invert[d[i]] = [i,]

    return invert