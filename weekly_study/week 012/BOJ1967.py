# 트리의 지름
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))

''' 시간초과
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    root, node, weight = map(int, sys.stdin.readline().strip().split())
    graph[root].append([node, weight])
    graph[node].append([root, weight])

def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1]*(n+1)
    visited[start] = 0
    m = 0
    while q:
        a = q.popleft()
        for e, w in graph[a]:
            if visited[e] == -1:
                visited[e] = visited[a]+w
                q.append(e)
                m = max(visited[e], m)

    return m

result = 0
for i in range(1, n+1):
    result = max(bfs(i), result)

print(result)
'''
