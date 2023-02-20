# 벽 부수고 이동하기 2
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start,K):
    visited = [[[-1] * C for _ in range(R)] for _ in range(K+1)]
    queue = deque()
    queue.append([0] + start)
    answer = R+C+1
    visited[0][start[0]][start[1]] = 0
    while queue:
        break_cnt, x, y = queue.popleft()
        if x == R-1 and y == C-1:
            return visited[break_cnt][x][y]+1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < R and 0 <= ay < C:
                if board[ax][ay] == 1 and break_cnt < K and visited[break_cnt + 1][ax][ay] == -1 :
                    queue.append([break_cnt+1,ax,ay])
                    visited[break_cnt+1][ax][ay] = visited[break_cnt][x][y] + 1
                elif board[ax][ay] == 0 and visited[break_cnt][ax][ay] == -1:
                    queue.append([break_cnt,ax,ay])
                    visited[break_cnt][ax][ay] = visited[break_cnt][x][y] + 1
    return -1
R,C,K = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(R)]

print(bfs([0,0],K))

''' 시간초과
from collections import deque

n, m, limit = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][z]은 불가능.
visited = [[[0] * (limit+1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c < limit :
                visited[nx][ny][c+1] = visited[a][b][c] + 1
                queue.append((nx, ny, c+1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))
'''