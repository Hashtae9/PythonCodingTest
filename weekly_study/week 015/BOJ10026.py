# 적록색약
from collections import deque


def bfs(x, y):
    queue.append((x, y))
    done.append((x, y))

    while queue:
        curr = queue.popleft()

        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]

            if (0 <= nx < N) and (0 <= ny < N) and ((nx, ny) not in done):
                if colors[nx][ny] == colors[curr[0]][curr[1]]:
                    queue.append((nx, ny))
                    done.append((nx, ny))


N = int(input())
colors = [list(input()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 정상인인 경우
queue = deque()
done = []
cnt_1 = 0

for i in range(N):
    for j in range(N):
        if (i, j) not in done:
            bfs(i, j)
            cnt_1 += 1


# 적록색맹인 경우
for i in range(N):
    for j in range(N):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

queue = deque()
done = []
cnt_2 = 0
for i in range(N):
    for j in range(N):
        if (i, j) not in done:
            bfs(i, j)
            cnt_2 += 1

print(cnt_1, cnt_2)

'''
import collections
import sys

n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph):
    visited = [[0]*n for _ in range(n)]
    count = 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: #방문한적 없음
                q = collections.deque()
                q.append([i, j])
                visited[i][j] = count
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x+dx[k]; ny = y+dy[k]
                        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                            visited[nx][ny] = count
                            q.append([nx, ny])
                count+=1
    return max(max(visited))

print(bfs(board), end=' ')

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G': board[i][j] = 'R'

print(bfs(board))
'''

