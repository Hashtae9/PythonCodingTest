# 가장 긴 증가하는 부분 수열
n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]: # 값이 이전값보다 크고 길이는 작은 case가 있는지 확인
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))