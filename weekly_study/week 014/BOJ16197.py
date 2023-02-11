# 두 동전
from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 벽이라면
                if board[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1
            else:  # 둘 다 빠진 경우 무시
                continue

    return -1

n, m = map(int, input().split())

coin = deque()
board = []
temp = []
for i in range(n):
    board.append(list(input().strip()))
    for j in range(m):
        if board[i][j] == "o":
            temp.append((i, j))

coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

print(bfs())

'''
import sys
from collections import deque
n, m = map(int, input().split())
road = [list(input()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
coin_count = 0
result = []

def bfs(x, y):
    q = deque()
    q.append([x, y])
    count = 0

    while q:
        if count == 10: return -1
        a, b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<= nx <n and 0 <= ny <m:
                if road[nx][ny] == '.':
                    count+=1
                    q.append([nx, ny])
            else:
                count+=1
                return count


for i in range(n):
    for j in range(m):
        if road[i][j] == 'o':
            coin_count+=1
            result.append(bfs(i, j))
        if coin_count == 2:
            print(min(result)); exit()'''