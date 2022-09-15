X = "abdehef"
Y = "abcieeejr"

m,n = len(X), len(Y)

def lcSubRec(X, Y, m, n, ans):
    if m==0 or n==0:
        return ans
    if X[m-1] == Y[n-1]:
        return lcSubRec(X, Y, m-1, n-1, ans+1)

    return max(ans, max(lcSubRec(X, Y, m-1,n, 0), lcSubRec(X, Y, m, n-1, 0)))

t = [[-1 for c in range(n+1)] for r in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0: t[i][j] = 0
        
def lcSubMemo(X, Y, m, n):
    if t[m][n] != -1:
        return t[m][n]

    if X[m-1] == Y[n-1]:        
        t[m][n] = 1 + lcSubMemo(X, Y, m-1, n-1)
        return t[m][n]
    else:
        t[m][n] = 0
        return t[m][n]

def lcSubDP(X, Y, m, n):
    t = [[0 for i in range(n+1)] for j in range(m+1)]

    ans = 0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0
            elif X[i-1] == Y[j-1]:
                t[i][j] = t[i-1][j-1] + 1
                ans = max(ans, t[i][j])
            else:
                t[i][j] = 0
    return ans

if __name__ == "__main__":
    print('Length Longest Common Subsequence Recursive')
    print(lcSubRec(X, Y, m, n, 0))
    print('Length Longest Common Subsequence Momoization')
    print(lcSubMemo(X, Y, m, n))
    print('Length Longest Common Subsequence DP')
    print(lcSubDP(X, Y, m, n))