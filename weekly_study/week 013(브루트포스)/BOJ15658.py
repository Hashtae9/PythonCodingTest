# 연산자 끼워넣기
N = int(input())
a = list(map(int,input().split()))
cnt = list(map(int,input().split()))
max_ans = -1000000000
min_ans = 1000000000

def dfs(idx, ans):
    global max_ans, min_ans

    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return

    if cnt[0] > 0:
        cnt[0] -= 1
        dfs(idx+1, ans+a[idx])
        cnt[0] += 1
    if cnt[1] > 0:
        cnt[1] -= 1
        dfs(idx+1, ans-a[idx])
        cnt[1] += 1
    if cnt[2] > 0:
        cnt[2] -= 1
        dfs(idx+1, ans*a[idx])
        cnt[2] += 1
    if cnt[3] > 0:
        cnt[3] -= 1
        dfs(idx+1, int(ans/a[idx]))
        cnt[3] += 1

dfs(1,a[0])
print(max_ans)
print(min_ans)

'''
import itertools
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().strip().split()))
check = list(map(int, sys.stdin.readline().strip().split()))
buho = []
for i in range(sum(check)):
    if i == 0:
        for _ in range(check[i]):
            buho.append('+')
    elif i == 1:
        for _ in range(check[i]):
            buho.append('-')
    elif i == 2:
        for _ in range(check[i]):
            buho.append('*')
    elif i == 3:
        for _ in range(check[i]):
            buho.append('/')
result = []

for i in list(itertools.permutations(buho, n-1)):
    a = num[0]
    for j in range(0, n-1):
        if i[j] == '+':
            a+=num[j+1]
        elif i[j] == '-':
            a-=num[j+1]
        elif i[j] == '*':
            a*=num[j+1]
        elif i[j] == '/':
            a= int(a/num[j+1])
    result.append(a)
print(max(result))
print(min(result))
'''