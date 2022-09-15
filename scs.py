from turtle import getscreen
from lcs import lcsDP


def scs(X,Y,m,n):
    lcsLength = lcsDP(X, Y, m, n)
    return m + n - lcsLength

def getSCS(X, Y, m, n):
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
    scs = ""
    i,j = m,n
    while i and j:
        if X[i-1]== Y[j-1]:
            scs += X[i-1]
            i -= 1
            j -= 1
        else:
            if t[i-1] > t[j-1]:
                scs += X[i-1]
                i -= 1
            else:
                scs += Y[j-1]
                j -= 1
    while i:
        scs += X[i-1]
        i-= 1
    while j:
        scs += X[j-1]
        j-= 1
    return scs[::-1]



if __name__ == "__main__":
    X = "abcdeeefgh"
    Y = "abcieejr"
    m,n = len(X), len(Y)
    print('Length of SCS')
    print(scs(X, Y, m, n))

    print("Shortest Common Sequence")
    print(getSCS(X, Y, m, n))
