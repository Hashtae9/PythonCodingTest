# 회의 준비
import sys
from collections import deque

INF = 100000
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

visited = [[] for _ in range(n+1)] # visited check

dist = [[INF]*(n+1) for i in range(n+1)] # 최단 경로를 담는 배열

# 123 4567 8
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    dist[a][b] = 1
    dist[b][a] = 1
    visited[a].append(b)
    visited[b].append(a)

# 그룹 찾기
v = [0]*(n+1)
count = 1
for i in range(1, n+1):
    if v[i] == 0:
        v[i] = count
        q = deque()
        for j in visited[i]:
            q.append(j)

        while q:
            element = q.popleft()
            if v[element]==0:
                v[element] = count
                for k in visited[element]:
                    q.append(k)
        count+=1
visited.clear()
team = []
for i in range(1, count):
    a = []
    for j in range(1, n+1):
        if v[j] == i:
            a.append(j)
    team.append(a)

def floyd_Warshall(d):

    for k in range(1, n+1): # 거치는 점
        for i in range(1, n+1): # i, j 체크
            for j in range(1, n+1):
                if dist[i][j] > d[i][k] + d[k][j]: # 최솟값으로 변경
                    d[i][j] = d[i][k] + d[k][j]
                if i == j:
                    d[i][j] = INF
    return d
dist = floyd_Warshall(dist)

for i in range(n+1):
    for j in range(n+1):
        if dist[i][j] == INF:
            dist[i][j] = 0

for line in dist:
    print(*line)

result = []
for t in team:
    check = sys.maxsize
    r = 0
    for i in t:
        if max(dist[i]) < check:
            check = max(dist[i])
            r = i
    result.append(r)
print(len(team))
for i in sorted(result):
    print(i)