# 레이저 통신
import collections
import sys

input = sys.stdin.readline
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

W, H = map(int, input().rstrip().split())
INF = H * W + 1
arr = list(input().rstrip() for _ in range(H))
visited = [[INF] * W for _ in range(H)]

# C 위치 두 개 찾기
c_index = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'C':
            c_index.append((i, j))
start = c_index[0]
target = c_index[1]


def sol():
    dq = collections.deque()
    dq.append((0, -1, start[0], start[1]))  # 거울 개수, 방향, 인덱스
    visited[start[0]][start[1]] = 0  # 출발점 다시 안 오게

    while dq:
        mirror_cnt, direction, i, j = dq.popleft()

        if i == target[0] and j == target[1]:  # 정답..!
            return mirror_cnt

        if visited[i][j] < mirror_cnt:  # 더 적은 거울 수로 이미 방문했으면
            continue

        visited[i][j] = mirror_cnt  # 꺼낸 후에 방문 체크

        for k in range(4):
            ni = i + direct[k][0]
            nj = j + direct[k][1]

            # 범위, 방문 체크, 벽 X
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] != '*':

                # 직진이면
                if k == direction or direction == -1:  # direction -1은 맨 처음에 사 방향으로 가는 것
                    dq.appendleft((mirror_cnt, k, ni, nj))  # 맨 앞에 붙이기(처음으로 나오게)

                # 꺾어야 하면(거울 필요)
                else:
                    dq.append((mirror_cnt + 1, k, ni, nj))  # 맨 뒤에 붙이기 (나중에 나오도록)


print(sol())

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    check = [[float('inf')] * W for _ in range(H)]
    check[sr][sc] = -1
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        if (r, c) == (gr, gc):
            return check[gr][gc]

        # 4방향으로 각각 직진
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while True:
                if not (0 <= nr < H and 0 <= nc < W):   # 격자 벗어나거나
                    break
                if A[nr][nc] == "*":                    # 벽 만나면 break
                    break
                if check[nr][nc] < check[r][c] + 1:     # 이동할 위치에 있는 거울이 현재까지 사용한 거울+1보다 작으면 갱신 X
                    break
                Q.append((nr, nc))                      # 새 위치 이동
                check[nr][nc] = check[r][c] + 1
                nr += dr[i]
                nc += dc[i]

# main
W, H = map(int, input().split())
A, C = [], []
sr, sc, gr, gc = 0, 0, 0, 0
for i in range(H):
    A.append(list(input().strip()))
    for j in range(W):
        if A[i][j] == "C":
            C.append((i, j))
(sr, sc), (gr, gc) = C
print(bfs())


'''
import collections
import sys

w, h = map(int, sys.stdin.readline().strip().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(h)]
lazer = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            lazer.append([i, j])

sx, sy = lazer[0]
ex, ey = lazer[1]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = collections.deque()
    q.append([sx, sy])
    visited = [[-1] * w for _ in range(h)]
    direction = [[-1] * w for _ in range(h)]  # 0(위) 1(아래) 2(좌) 3(우)
    visited[sx][sy] = 0
    direction[sx][sy] = 5  # 시작점

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:  # 다음스텝이 범위 내
                if visited[nx][ny] == -1:  # 방문x
                    if i == direction[x][y]:  # 방향을 쭉 이어감
                        direction[nx][ny] = i
                        visited[nx][ny] = visited[x][y]
                        q.appendleft([nx, ny])
                    # i는 다음방향, direction[x][y]는 이 이동 이전의 방향
                    elif i != direction[x][y]:  # 방향이 바뀜
                        visited[nx][ny] = visited[x][y] + 1
                        direction[nx][ny] = i
                        q.append([nx, ny])
                elif visited[nx][ny] != -1 and visited[nx][ny] > visited[x][y]:
                    if i == direction[x][y]:  # 방향을 쭉 이어감
                        direction[nx][ny] = i
                        visited[nx][ny] = visited[x][y]
                        q.appendleft([nx, ny])
                    elif i != direction[x][y]:  # 방향이 바뀜
                        visited[nx][ny] = visited[x][y] + 1
                        direction[nx][ny] = i
                        q.append([nx, ny])
    print(visited)
bfs()

'''