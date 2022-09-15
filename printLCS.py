
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
    lcs = ""
    i,j = m,n
    while i and j:
        if X[i-1]==Y[j-1]:
            lcs += X[i-1]
            i -= 1
            j -= 1
        else:
            if t[i-1][j] > t[i][j-1]:
                i -= 1
            else: j -= 1
    while i:
        lcs += X[i-1]
        i -= 1
    while j:
        lcs += Y[i-1]
        j -= 1
    return lcs[::-1]



if __name__== "__main__":
    X = "abcdeeefgh"
    Y = "abcieejr"
    m,n = len(X), len(Y)
    print('Printing LCS')
    print(lcsDP(X, Y, m, n))