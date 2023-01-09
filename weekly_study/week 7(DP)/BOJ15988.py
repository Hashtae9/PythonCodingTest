#1, 2, 3 더하기 3
n = int(input())
list = []
m = 0

for _ in range(n):
    a = int(input())
    m = max(a, m)
    list.append(a)

dp = [0 for i in range(m+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, m+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

for i in list:
    print(dp[i]%1000000009)