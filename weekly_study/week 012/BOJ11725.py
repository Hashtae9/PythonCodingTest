# 트리의 부모 찾기
import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def bfs():
    q = deque()
    q.append(1)

    while q:
        num = q.popleft()
        for i in graph[num]:
            if visited[i] == 0:
                parent[i] = num
                q.append(i)
        visited[num] = 1
bfs()
print('\n'.join(map(str, parent[2:])))