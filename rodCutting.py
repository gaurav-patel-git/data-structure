# here L(lenght of rod)

length = [1,2,3,4,5,6,7,8,9,10]  # if lenght array not given then make one from 1 to L
price = [1,1,5,4,1,3,6,4,6,9]  # value array
L = 10  # knapsack capacity
n = len(length)

def rodCutting(L, n, length, price):
    t = [[0 for c in range(L+1)] for r in range(len(length)+1)]
    for i in range(1,n+1):
        for j in range(1,L+1):
            if length[i-1]<=j:
                t[i][j] = max(t[i-1][j], price[i-1] + t[i][j-length[i-1]])
            else: 
                t[i][j] = t[i-1][j]
    return t[n][L]


if __name__ == "__main__":    
    print('Rod Cutting max profit')
    print(rodCutting(L, n, length, price))