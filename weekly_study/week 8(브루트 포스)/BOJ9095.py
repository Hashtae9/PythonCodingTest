# 1, 2, 3 더하기

n = int(input())
for _ in range(n):
    a = int(input())
    dp = [0 for j in range(12)]
    dp[0] = 1; dp[1] = 1; dp[2] = 2
    if a <= 2: print(dp[a]); continue
    for i in range(3, a+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[a])
