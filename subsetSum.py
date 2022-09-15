def subsetSum(arr, S):
    n = len(arr)
    t = [[None for c in range(S+1)] for r in range(n+1)]

    for r in range(n+1):
        for c in range(S+1):
            if r==0:
                t[r][c] = False
            if c==0:
                t[r][c] = True
    # print(t)
    for i in range(1,n+1):
        for j in range(1,S+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]

    return t[n][S], t

    
if __name__=="__main__":
    arr = [1,2,3,4,5]
    S = 5
    print('Subset Sum')
    print(subsetSum(arr, S))