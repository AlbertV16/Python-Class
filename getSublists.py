def getSublists(L, n):
    count = 0
    sublist = []
    while count +n <= len(L):
        sublist.extend([L[count:count+n]])
        count += 1
        
    return sublist