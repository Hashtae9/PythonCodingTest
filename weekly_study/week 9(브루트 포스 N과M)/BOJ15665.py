#N과 M 11
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            temp.pop()

dfs()

'''
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
result = []

def dfs():
    if len(s) == m:
        result.append(str(s).strip('[').strip(']').replace(',', ''))
        return

    for i in arr:
        s.append(i)
        dfs()
        s.pop()
dfs()

for i in sorted(list(set(result))):
    print(i)
'''

'''
from itertools import product

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cmb = list(product(a, repeat=m))
ans = []

for c in cmb:
    ans.append(c)

ans = sorted(list(set(ans)))  #중복 제거 후 정렬

for c in ans:
    for i in c:
        print(i, end=' ')
    print()
'''