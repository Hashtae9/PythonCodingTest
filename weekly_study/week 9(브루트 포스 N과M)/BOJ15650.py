# n과 m 2
import itertools

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
com = list(itertools.combinations(arr, m))
for i in com:
    s = str(i).strip('(').strip(')').replace(',', '')
    print(s)

'''
# 15650번
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
'''