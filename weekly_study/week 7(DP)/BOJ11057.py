#오르막수
n = int(input())

dp = [[0 for i in range(10)] for j in range(n+1)]
dp[1] = [1 for _ in range(10)]
for i in range(2, n+1):
    for j in range(10):
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][k]
print(sum(dp[n])%10007)