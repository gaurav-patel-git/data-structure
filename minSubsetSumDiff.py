def minSubsetSumDiff(arr):
    n = len(arr)
    S = sum(arr)
    s1 = (S//2)
    t = [[None for c in range(s1+1)] for r in range(n+1)]
    for i in range(n+1):
        for j in range(s1+1):
            if i==0:
                t[i][j] = False
            if j ==0:
                t[i][j] = True
    for i in range(1,n+1):
        for j in range(1,s1+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    lastRow = t[n]
    lastTrue = None
    for ind, flag in enumerate(lastRow):
        if flag: lastTrue = ind
    s2 = S-lastTrue
    s1 = lastTrue

    return(abs(s1-s2))

if __name__=="__main__":
    print('Minimum Subset Sum Difference <<or>> Target Sum')
    arr = [1,2,3,50]
    print(arr)
    print(minSubsetSumDiff(arr))    
        


