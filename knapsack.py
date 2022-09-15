W= 80
wt = [22,54,8,16]
val = [65,75,45,9]
n = len(val)


def knapSackRec(W, n):    
    if n==0 or W==0:
        return 0
    if wt[n-1] <= W:
        return max(
            val[n-1] + knapSackRec(W-wt[n-1], n-1),
            knapSackRec(W, n-1)
            )   
    else:
        return knapSackRec(W, n-1)

# you can even fill the matrix with 0 no issues
# in that case you don't have to do initialization
t = [[-1 for c in range(W+1)] for r in range(n+1)]

# initialization
for r in range(n+1):
    for c in range(W+1):
        if r == 0 or c==0:
            t[r][c] = 0




def knapSackMemo(W, n):
    if n==0 or W==0:
        return 0

    if t[n][W]!=-1: return t[n][W]
    if wt[n-1] <= W:
        t[n][W] =  max(
            val[n-1] + knapSackMemo(W-wt[n-1], n-1),
            knapSackMemo(W, n-1)
            )   
        return t[n][W]
    else:
        t[n][W] = knapSackMemo(W, n-1)
        return t[n][W]


def knapSackDP(W, n, wt, val):
    t = [[0 for c in range(W+1)] for r in range(len(wt)+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                t[i][j] = max(t[i-1][j], val[i-1] + t[i-1][j-wt[i-1]])
            else: 
                t[i][j] = t[i-1][j]
    return t[n][W]

if __name__ == "__main__":    
    print('Knapsack recursion')
    print(knapSackRec(W, n))

    print('knapsack Memoization')
    print(knapSackMemo(W, n))
                
    print("Knapsack DP")
    print(knapSackDP(W, n, wt, val))