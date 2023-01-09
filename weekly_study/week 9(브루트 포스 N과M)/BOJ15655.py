#n과m 6
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s=[]
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n):
        s.append(arr[i])
        dfs(i+1)
        s.pop()
dfs(0)
'''
import itertools
n, m = map(int, input().split())
arr = list(map(int, input().split()))
con = itertools.combinations(sorted(arr), m)
for i in con:
    print(str(i).strip('(').strip(')').replace(',', ''))
'''