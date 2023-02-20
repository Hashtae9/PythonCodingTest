# 탈출
from collections import deque

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
# 좌표 위에 뭔가 있으면 True로 방문 처리
visited = [[False] * C for _ in range(R)]

sonic = deque()  # 고슴도치
water = deque()  # 물
count = 0  # 시간(초) 카운트

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물, 고슴도치 좌표 추가. 방문 True로 설정
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            water.append((i, j))
            visited[i][j] = True
        elif graph[i][j] == 'S':
            sonic.append((i, j))
            visited[i][j] = True
        elif graph[i][j] == 'X':
            visited[i][j] = True

# 고슴도치 이동가능할때마다 반복문
while sonic:
    # 물 현황 구현
    for i in range(len(water)):
        w_x, w_y = water.popleft()
        for j in range(4):
            nx = w_x + dx[j]
            ny = w_y + dy[j]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    water.append((nx, ny))
                    graph[nx][ny] = '*'
                    visited[nx][ny] = True

    # 물 확장시 시간 추가. 고슴도치는 물이 찰 예정 칸으로 이동할 수 없기 때문에 고슴도치 구현보다 먼저 카운트
    count += 1

    # 고슴도치 움직이는 로직 구현
    for _ in range(len(sonic)):
        s_x, s_y = sonic.popleft()
        for i in range(4):
            nx = s_x + dx[i]
            ny = s_y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] =='.' and visited[nx][ny] == False:
                    sonic.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 'D':
                    print(count)
                    exit()

print('KAKTUS')



'''
import collections
import sys

r, c = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for i in range(r)] # r, c
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
water = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'D':
            end = [i, j]
        elif board[i][j] == 'S':
            gosm = [i, j]
        elif board[i][j] == '*':
            water.append([i, j])

def bfs():
    global board
    q = collections.deque()
    q.append([-1, -1])
    q.append(gosm)
    visited = [[-1]*c for _ in range(r)]
    visited[gosm[0]][gosm[1]] = 0
    w = water

    while q:
        x, y = q.popleft()
        new_w = []
        if x == -1 and y == -1:
            #물 먼저 퍼지기
            for wat in w:
                for i in range(4):
                    wx = wat[0]+dx[i]; wy = wat[1]+dy[i]
                    if not (0<=wx<r and 0<=wy<c): continue
                    if board[wx][wy] != 'D' and board[wx][wy] != 'X' and board[wx][wy] != '*':
                        board[wx][wy] = '*'
                        new_w.append([wx, wy])
            w = new_w
            continue
        # 고슴도치 이동
        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]
            if not (0<=nx<r and 0<=ny<c): continue
            if nx == end[0] and ny == end[1]: return visited[x][y]+1
            if board[nx][ny] != 'X' and board[nx][ny] != '*' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx, ny])
        q.append([-1, -1])
        w = new_w
    return "KAKTUS"
print(bfs())'''