# 이친수

n = int(input())

dp = [[0 for i in range(2)] for j in range(91)]

dp[1] = [0, 1] # 1만 가능
dp[2] = [1, 0] # 10 만 가능
#dp[3] = [1, 1] # 101 100
#dp[4] = [] # 1010 1000 1001
for i in range(3, 91):
    dp[i][1] = dp[i-1][0]
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
print(sum(dp[n]))