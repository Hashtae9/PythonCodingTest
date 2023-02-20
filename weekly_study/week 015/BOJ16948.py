# 데스 나이트
from collections import deque

n = int(input())
r1x, r1y, r2x, r2y = map(int, input().split())
visited = [[-1]*n for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs():
    q = deque()
    q.append([r1x, r1y])
    visited[r1x][r1y] = 0

    while q:
        a, b = q.popleft()
        for i in range(6):
            nx = a+dx[i]; ny = b+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1: #범위안이고 방문x
                if nx == r2x and ny == r2y:
                    return visited[a][b] + 1
                else:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append([nx, ny])

    return -1

print(bfs())