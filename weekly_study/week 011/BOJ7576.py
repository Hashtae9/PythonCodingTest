# 토마토
from collections import deque
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
result = 0
def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y]+1
                queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])
bfs()

for line in tomato:
    for t in line:
        if t == 0:
            print(-1); exit()
    result = max(result, max(line))
print(result-1)
