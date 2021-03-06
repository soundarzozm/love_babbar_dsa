import numpy as np

def subsetSum(wt, n, W):

    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wt[i-1]<=j:
                t[i][j] = (t[i][j-wt[i-1]]) + (t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    return t[n][W]


if __name__=="__main__":
    coins = [1, 2, 3]
    sum = 5
    n = len(coins)

    t = [[None] * (sum+1)] * (n+1)

    t = np.array(t)

    print(subsetSum(coins, n, sum))