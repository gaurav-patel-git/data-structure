W= 7 
wt = [1,2,3,4]
val = [5,1,5,20]
n = len(val)


def unboundedKnapsackRec(W, n):
    if n==0 or W==0:
        return 0
    if wt[n-1] <= W:
        return max(
            val[n-1] + unboundedKnapsackRec(W-wt[n-1], n),
            unboundedKnapsackRec(W, n-1)
            )   
    else:
        return unboundedKnapsackRec(W, n-1)

# you can even fill the matrix with 0 no issues
# in that case you don't have to do initialization
t = [[-1 for c in range(W+1)] for r in range(n+1)]

# initialization
for r in range(n+1):
    for c in range(W+1):
        if r == 0 or c==0:
            t[r][c] = 0


def unboundedknapsackMemo(W, n):
    if n==0 or W==0:
        return 0

    if t[n][W]!=-1: return t[n][W]
    if wt[n-1] <= W:
        t[n][W] =  max(
            val[n-1] + unboundedknapsackMemo(W-wt[n-1], n),
            unboundedknapsackMemo(W, n-1)
            )   
        return t[n][W]
    else:
        t[n][W] = unboundedknapsackMemo(W, n-1)
        return t[n][W]


def unboundedKnapsackDP(W, n, wt, val):
    t = [[0 for c in range(W+1)] for r in range(len(wt)+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                t[i][j] = max(t[i-1][j], val[i-1] + t[i][j-wt[i-1]])
            else: 
                t[i][j] = t[i-1][j]
    return t[n][W]



if __name__ == "__main__":    
    print('Unbounded knapsack recursion')
    print(unboundedKnapsackRec(W, n))

    print('Unbounded knapsack Memoization')
    print(unboundedknapsackMemo(W, n))
                
    print("Unbounded Knapsack DP")
    print(unboundedKnapsackDP(W, n, wt, val))