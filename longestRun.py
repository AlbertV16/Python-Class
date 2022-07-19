def longestRun(L):
    
    longestrun = 1
    for i in range(0,len(L)):
        count = 1
        for k in range(i,len(L)-1):
            if L[k+1] >= L[k]:
                count += 1
            else:
                break
        if count > longestrun:
            longestrun = count
    return longestrun