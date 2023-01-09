# 합분해
n, k = map(int, input().split())

dp =[[0 for _ in range(201)] for _ in range(201)]
dp[1] = [1 for _ in range(n+1)]

for i in range(1, k+1):
    for j in range(n+1):
        for m in range(j+1):
            dp[i][j] += dp[i-1][j-m]
        dp[i][j] %= 1000000000

print(dp[k][n])
# [4][6] = 35 34 33 32 31 30