# 연속합
n = int(input())
a= list(map(int, input().split()))
dp = []
dp.append(a[0])
for i in range(1, n):
    dp.append(max(dp[i-1] + a[i], a[i])) # 다 더한값이랑 현재값하나랑 값 비교
print(max(dp))
