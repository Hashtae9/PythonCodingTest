# 벽 부수고 이동하기 3
import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

if n == m == 1:
    print(1)
    exit()

road = [[c for c in input()] for _ in range(n)]

visited = [[k + 1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque([(0, 0, 0)])
res = 1

is_night = False
while q:
    q_length = len(q)
    for _ in range(q_length):
        r, c, w = q.popleft()

        if r == n - 1 and c == m - 1:
            print(res)
            exit()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if not(0 <= nr < n and 0 <= nc < m):
                # 맵의 범위를 벗어난다면
                continue

            if visited[nr][nc] <= w:
                # 이미 더 적은 방법으로 도달할 수 있다면
                continue

            # 밤이 아니고
            if not is_night:
                if road[nr][nc] == '0': # 갈 수 있는 길이라면
                    visited[nr][nc] = w
                    q.append((nr, nc, w))
                else:
                    if w >= k:
                        continue
                    visited[nr][nc] = w
                    q.append((nr, nc, w + 1))
            else:
                if road[nr][nc] == '0':
                    visited[nr][nc] = w
                    q.append((nr, nc, w))
                else:
                    q.append((r, c, w))

    is_night = not is_night
    res += 1
print(-1)

'''
import collections
import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(n)]
visited = [[[0]*m for _ in range(n)] for j in range(k+1)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = collections.deque()
    q.append([0, 0, 0, 0]) # k n m check
    visited[0][0][0] = 1

    while q:
        block, x, y, check = q.popleft()
        if x == n-1 and y == m-1: return visited[block][x][y];

        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[block][nx][ny] == 0: #우선 범위 내에 있음
                if check == 0:
                    if graph[nx][ny] == 1 and block != k: #낮이고 아직 부술수 있음
                        visited[block+1][nx][ny] = visited[block][x][y]+1
                        q.append([block+1, nx, ny, 1])
                    elif graph[nx][ny] == 0:
                        visited[block][nx][ny] = visited[block][x][y]+1
                        q.append([block, nx, ny, 1])
                else: #밤
                    if graph[nx][ny] == 0:
                        visited[block][nx][ny] = visited[block][x][y]+1
                        q.append([block, nx, ny, 0])
                    elif graph[nx][ny] == 1:
                        visited[block][x][y] = visited[block][x][y]
                        q.append([block, x, y, 0])
    return -1
print(bfs())
'''