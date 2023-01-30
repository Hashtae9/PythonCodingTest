#알고스팟
# BFS 벽을 최소 몇 개 부수어야 하는가?
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]  # 가중치

q = deque()
q.append((0,0))
dist[0][0] = 0
while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if arr[nx][ny] == 0: #미로값 == 0
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
print(dist[n-1][m-1])

'''
from collections import deque

n, m = map(int, input().split())
miro = [list(input()) for _ in range(m)]
visisted = [[-1 for i in range(n)] for j in range(m)]
broken = [[0 for i in range(n)] for j in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    q = deque()
    q.append([0, 0])

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            print(broken[x][y])
            return

        for i in range(4):
            if 0<= x+dx[i] <n and 0<= y+dy[i] < m and visisted[x+dx[i]][y+dy[i]] == -1:
                if miro[x+dx[i]][y+dy[i]] == 1: #벽을 부수는 경우
                    broken[x+dx[i]][y+dy[i]] = broken[x][y] + 1
                    q.append([x+dx[i], y+dy[i]])
                elif miro[x+dx[i]][y+dy[i]] == 0:
                    broken[x+dx[i]][y+dy[i]] = broken[x][y]
                    q.append([x+dx[i], y+dy[i]])
bfs()
'''