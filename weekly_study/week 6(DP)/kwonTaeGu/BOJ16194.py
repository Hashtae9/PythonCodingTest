# 카드 구매하기 2
import sys
n = int(sys.stdin.readline())
card_cost = list(map(int, sys.stdin.readline().split()))

dp = [0]*(n+1)
#dp[2] = dp[1]+card_cost[i], card_cost[2]와의 비교
dp[0] = card_cost[0]
dp[1] = card_cost[0]

for i in range(2, n+1):
    dp[i] = card_cost[i-1]
    for j in range(1, i+1):
        dp[i] = min(dp[i-j] + card_cost[j-1], dp[i])
print(dp[n])