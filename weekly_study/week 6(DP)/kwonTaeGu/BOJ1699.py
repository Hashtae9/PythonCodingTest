# 제곱수의 합

n = int(input())
dp = [x for x in range (n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])

'''
n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])
'''
# 1 4 9 16
#  3 5 7