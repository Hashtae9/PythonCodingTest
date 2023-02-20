#연구소
import copy
import itertools
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
blank = []
poison = []
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def fillbox(g):
    q = deque()
    for i in poison:
        q.append(i)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 0:
                q.append([nx, ny])
                g[nx][ny] = 2

    count = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0: count+=1
    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append([i, j])
        if graph[i][j] == 2:
            poison.append([i, j])

com = list(itertools.combinations(blank, 3))
count = []
for b1, b2, b3 in com:
    x1, y1 = b1
    x2, y2 = b2
    x3, y3 = b3
    graph[x1][y1] = 1
    graph[x2][y2] = 1
    graph[x3][y3] = 1
    result.append(fillbox(copy.deepcopy(graph)))
    graph[x1][y1] = 0
    graph[x2][y2] = 0
    graph[x3][y3] = 0
print(max(result))
