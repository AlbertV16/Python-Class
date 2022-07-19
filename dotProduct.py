def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    returns the dot product of listA and listB
    '''
    C = 0
    for i in range(0, len(listA)):
        C += listA[i] * listB[i]
    return C