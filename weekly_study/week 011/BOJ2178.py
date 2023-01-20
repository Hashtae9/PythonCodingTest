#미로 탐색
from collections import deque
N, M = map(int,input().split())

# N x M 방문 유무 확인 행렬 생성
visited = [[False] * M for _ in range(N)]

# N줄 만큼 입력
graph = [list(map(int, input().strip())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 끔점이 나오면 끝내주고, 마지막에 누적된 합을 print
            if x == N -1 and y == M-1:
                print(graph[N -1][M-1])
                break

            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    # 이동할 자리에 현재 누적된 값 + 1을 해주면서 누적해 나간다.
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])


bfs(0,0)

'''
import copy
import sys

n, m = map(int, input().split())
miro = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
result = sys.maxsize

def dfs(i, j, method_count, visit):
    global result
    if i == -1 or j == -1 or i == n or j == m:
        return

    if i == n-1 and j == m-1:
        result = min(result, method_count+1)
        return

    if visit[i][j] == False:

        visit[i][j] = True
        if miro[i][j] == '1':
            v = copy.deepcopy(visit)
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for k in range(4):
                dfs(i+dx[k], j+dy[k], method_count+1, v)
dfs(0, 0, 0, visited)
print(result)
'''