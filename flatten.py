def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flatlist = []
    if aList == []:
        return flatlist

    for i in range(0,len(aList)):
        if type(aList[i]) == str:
            flatlist.extend([aList[i]])
        elif type(aList[i]) == int:
            flatlist.extend([aList[i]])
        elif type(aList[i]) == list:
            flatlist.extend(flatten(aList[i]))
        
    return flatlist