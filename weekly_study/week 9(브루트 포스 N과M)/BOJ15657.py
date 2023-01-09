#N과 M 8
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s=[]
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n):
        s.append(arr[i])
        dfs(i)
        s.pop()
dfs(0)