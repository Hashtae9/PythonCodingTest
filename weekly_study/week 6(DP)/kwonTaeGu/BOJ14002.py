#가장 긴 증가하는 부분수열 4
n = int(input())
a = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
x = max(dp)
result = []
for i in range(n-1, -1, -1): # n-1 부터 0까지 1씩 감소
    if dp[i] == x:
        result.append(a[i])
        x-=1
result.reverse()
print(' '.join(list(map(str, result))))