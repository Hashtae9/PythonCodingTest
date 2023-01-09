# n과 m 5
n, m = map(int, input().split())
arr = list(map(int, input().split()))

s=[]

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in sorted(arr):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
'''
# n과 m 5
import itertools
n,m = map(int, input().split())
arr = list(map(int, input().split()))
con = list(itertools.permutations(sorted(arr), m))
for i in con:
    print(str(i).strip('(').strip(')').replace(',', ''))
'''