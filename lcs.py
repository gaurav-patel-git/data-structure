# def lcsRec(X, Y, m, n):
#     if m==0 or n==0:
#         return 0
#     if X[m-1] == Y[n-1]:
#         return 1 + lcsRec(X, Y, m-1, n-1)

#     else:
#         return max(lcsRec(X, Y, m-1, n),
#                    lcsRec(X, Y, m, n-1))

        
# def lcsMemo(X, Y, m, n):
#     if t[m][n] != -1:
#         return t[m][n]

#     if X[m-1] == Y[n-1]:        
#         t[m][n] = 1 + lcsMemo(X, Y, m-1, n-1)
#         return t[m][n]
#     else:
#         t[m][n] = max(lcsMemo(X, Y, m-1, n),
#                       lcsMemo(X, Y, m, n-1))
        # return t[m][n]

def lcsDP(X, Y, m, n):
    t = [[None for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0: t[i][j] = 0

    for i in range(1, m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    ans = 0
    for i in range(n+1):
        for j in range(m+1):
            ele = t[i][j]
            if ele == 5: ans += 1
    return ans

if __name__ == "__main__":
    X = "abcdeeefgh"
    Y = X[::-1]
    m,n = len(X), len(Y)

    t = [[-1 for c in range(n+1)] for r in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0: t[i][j] = 0
    # print('Length Longest Common Subsequence Recursive')
    # print(lcsRec(X, Y, m, n))
    # print('Length Longest Common Subsequence Momoization')
    # print(lcsMemo(X, Y, m, n))
    print('Length Longest Common Subsequence DP')
    print(lcsDP(X, Y, m, n))