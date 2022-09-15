

coin = [1,3,6, 2, 8, 4]  
S = 20  # sum you need to achieve

def coinChangeMaxWays(S,coin):
    n = len(coin)
    t = [[None for c in range(S+1)] for r in range(n+1)]

    for i in range(n+1):
        for j in range(S+1):
            if i==0: t[i][j] = 0
            if j==0: t[i][j] = 1

    for i in range(1,n+1):
        for j in range(1,S+1):
            if coin[i-1] <= j:
                t[i][j] = t[i-1][j] + t[i-1][j-coin[i-1]]
            else:
                t[i][j] = t[i-1][j]
    return t[n][S]


if __name__ == "__main__":
    # count subset sum in unbounded knapsack
    print("Coin change Maximum number of ways")
    print(coinChangeMaxWays(S, coin))
