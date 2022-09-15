from lcs import lcsDP

def minInsDel(A, B):
    m = len(A)
    n = len(B)
    lcsLength = lcsDP(A, B, m, n)
    insertitions = len(B) - lcsLength
    deletion = len(A) - lcsLength

    return insertitions, deletion


if __name__ == "__main__":
    A = "abcdeeefgh"
    B = "abcieejr"
    print('Minimum number of insertition and deletion to convert A -> B')
    print(minInsDel(A,B))    