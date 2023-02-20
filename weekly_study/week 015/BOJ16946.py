# 벽 부수고 이동하기4
from collections import deque
input = __import__('sys').stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            q.append((ni, nj))
            cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1
info = {}
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(n):
    for j in range(m):
        addList = set()
        if graph[i][j]:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                graph[i][j] += info[add]
                graph[i][j] %= 10

for g in graph:
    print("".join(map(str, g)))

''' 시간초과
import collections
import copy
import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    q = collections.deque()
    q.append([a, b])
    visited = [[-1]*m for _ in range(n)]
    visited[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1 and graph[nx][ny] == 0:
                visited[nx][ny] = 0
                count+=1
                q.append([nx, ny])
    return count


result = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = 0
            result[i][j] = bfs(copy.deepcopy(board), i, j)
            board[i][j] = 1
        else:
            result[i][j] = 0

for i in result:
    print(''.join(map(str, i)))

'''