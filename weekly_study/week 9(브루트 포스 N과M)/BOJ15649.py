# N과 M

import itertools

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
C = list(itertools.permutations(arr, m))

for i in C:
    print(str(i).strip('(').strip(')').replace(',', ''))

'''
n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
'''