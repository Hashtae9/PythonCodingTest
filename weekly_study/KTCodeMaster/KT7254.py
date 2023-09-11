# 탈출사건
import copy
import sys
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().split())
zoo = []
for i in range(n):
    zoo.append(list(map(int, sys.stdin.readline().split())))

zag = []
zero = []

for i in range(n):
    for j in range(m):
        if zoo[i][j] == 0:
            zero.append([i, j])
        elif zoo[i][j] == 2:
            zag.append([i, j])

result = []
com = list(combinations(zero, 3))

for i in com:
    x1, y1 = i[0]; x2, y2 = i[1]; x3, y3 = i[2]
    zoo_copy = copy.deepcopy(zoo)

    # 벽 세우기
    zoo_copy[x1][y1] = 1
    zoo_copy[x2][y2] = 1
    zoo_copy[x3][y3] = 1

    # 재규어 이동 확인
    q = deque()
    for z in zag:
        q.append(z)

    while q:
        x, y = q.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for index in range(4):
            nx = x+dx[index]; ny = y+dy[index]
            if 0<= nx <n and 0<= ny <m: # 범위 내
                if zoo_copy[nx][ny] == 0:# 이동가능
                    zoo_copy[nx][ny] = 1
                    q.append([nx, ny])

    # 0 개수 count
    count = 0
    for k in range(n):
        for l in range(m):
            if zoo_copy[k][l] == 0:
                count += 1
    result.append(count)

print(max(result))
