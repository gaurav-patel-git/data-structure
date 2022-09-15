from lcs import lcsDP
from lcSub import lcSubDP

def lps(X):
    Y = X[::-1]
    m,n = len(X), len(Y)
    return lcsDP(X, Y, m, n)

def lpSub(X):
    Y = X[::-1]
    m,n = len(X), len(Y)
    return lcSubDP(X, Y, m, n)

def minDelToPldrm(X):
    return len(X) - lps(X)

if __name__ == "__main__":
    X = "abcdeeefghba"
    print("Longest Palindormic Subsequecnce")
    print(lps(X))

    print("Longest Palindormic Substring")
    print(lpSub(X))

    print("Minimum number of inserition/deletion to make a string palindrome")
    print(minDelToPldrm(X))