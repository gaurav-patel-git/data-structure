def countSubsetSum(arr, S):
    n = len(arr)
    t = [[None for i in range(S+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(S+1):
            if i==0:
                t[i][j] = 0
            if j==0:
                t[i][j] = 1
    for i in range(1,n+1):
        for j in range(1,S+1):
            if arr[i-1]<=j:
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    return t[i][S]


if __name__=="__main__":
    arr = [1,2,3,5,5,2,2,2,2]
    S = 20
    print(countSubsetSum(arr, S))    
    