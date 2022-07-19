def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter = {}
    diff = {}
    for i in d1:
        for k in d2:
            if i in d1 and i in d2:
                inter[i] = f(d1[i], d2[i])
            else:
                diff[i] = d1[i] 
            if k not in d1:
                diff[k] = d2[k]

    intdiff = (inter,diff)
    return intdiff