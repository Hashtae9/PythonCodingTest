#트리의 지름
from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, read().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)

'''
import sys
sys.setrecursionlimit(100000)

v = int(sys.stdin.readline())
graph = [[] for i in range(v+1)] # index:정점, [연결된 정점, 정점 간의 거리]
for _ in range(v):
    l = list(map(int, sys.stdin.readline().strip().split()))
    root = l[0]
    for i in range(1, len(l), 2):
        if l[i] == -1:
            break
        graph[root].append([l[i], l[i+1]])
result = []

def dfs(idx, d, visited):
    for index, dist in graph[idx]:
        if index not in visited:
            d += dist
            visited.append(index)
            dfs(index, d, visited)
            visited.remove(index)


for i in range(1, v+1):
    dfs(i, 0, [i])
print(result)
'''