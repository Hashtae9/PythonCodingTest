#n과m 7
m,n = map(int, input().split())
arr = sorted(list(map(int, input().split())))

s=[]

def dfs():
    if len(s) == n:
        print(' '.join(map(str, s)))
        return

    for i in arr:
        s.append(i)
        dfs()
        s.pop()
dfs()