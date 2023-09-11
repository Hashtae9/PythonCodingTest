# 막사 정찰
import sys

n, p = map(int, sys.stdin.readline().split())
road = [[] for i in range(n+1)]

for i in range(p):
    a, b = map(int, sys.stdin.readline().split())
    road[a].append(b)
    road[b].append(a)

visited = [False]*(n+1)

def dfs1(visited, road, m, count):
    if m == 1: return count+1
    visited[m] = True

    for i in road[m]:
        if not visited[i]:
            count = max(count, dfs1(visited, road, i, count))
    return count

def dfs2(visited, road, m, count):
    if m == 2: return count+1
    visited[m] = True

    for i in road[m]:
        if not visited[i]:
            count = max(count, dfs2(visited, road, i, count))
    return count

result1 = dfs1(visited, road, 2, 0)
visited = [False]*(n+1)
result2 = dfs2(visited, road, 1, 0)
print(min(result1, result2))