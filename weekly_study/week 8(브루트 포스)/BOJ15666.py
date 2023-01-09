#n과 m 12
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    rem = 0
    for i in range(start, n):
        if arr[i] != rem:
            temp.append(arr[i])
            rem = arr[i]
            dfs(i)
            temp.pop()
dfs(0)