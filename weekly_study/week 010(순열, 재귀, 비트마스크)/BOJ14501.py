#퇴사
n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)

for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])

'''
1. 상담이 끝나는 날이 n을 넘어가게 되면 일을 맡을 수 없기 때문에 dp[i] = dp[i + 1]

2. 그 외의 부분에는

(1)[현재 일을 맡았을 때 들어오는 보상 + 현재 일을 끝낸 다음날에 쌓여있는 보상]

(2)일을 맡지 않을 경우 보상

둘을 비교

max(p_list[i] + answer[i + t_list[i]], answer[i + 1])
'''

'''
import sys

n = int(input())
day = []
money = []
for _ in range(n):
    a = list(map(int, input().split()))
    day.append(a[0])
    money.append(a[1])

s1=[]
s2=[]
s3=[]
result = 0
def dfs(start):
    global result
    if sum(s1) > n:
        return
    elif sum(s1) == n:
        result = max(result, sum(s2))
        return

    for i in range(start, n):
        if s1[-1] == start:
            dif = start - s1[-1]
        s1.append(day[i])
        s2.append(money[i])
        s3.append(0)
        dfs(i+day[i])
        s1.pop()
        s2.pop()
        s3.pop()

dfs(0)
print(result)

'''