# 움직이는 미로 탈출
from collections import deque


dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]

def bfs():
    queue = deque()
    queue.append((7,0))
    time = 0

    while queue:
        visited = [[False]*8 for _ in range(8)]

        for _ in range(len(queue)):
            a, b = queue.popleft()
            #print(time, (a,b))
            if matrix[a][b] == -1:
                continue
            if (a,b) == (0,7):
                return 1

            for i in range(9):
                nx = dx[i] + a
                ny = dy[i] + b

                if not (0 <= nx < 8 and 0 <= ny < 8):
                    continue
                if matrix[nx][ny] == -1 or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                queue.append((nx,ny))

        matrix.pop()
        matrix.appendleft([0]*8)

        time += 1
        if time == 9:
            return 1
    return 0

matrix = deque([[]for _ in range(8)])
for i in range(8):
    for j in input():
        if j == '.':
            matrix[i].append(0)
        else:
            matrix[i].append(-1)

print(bfs())
'''
import collections
import sys

graph = [list(sys.stdin.readline().strip()) for i in range(8)]
dx = [1, -1, 0, 0, 1, -1, 1, -1, 0]
dy = [0, 0, -1, 1, 1, 1, -1, -1, 0]

def bfs():
    q = collections.deque()
    q.append([7, 0]) # 왼쪽 아래 스타트
    block = []
    for i in range(8):
        for j in range(8):
            if graph[i][j]=='#': block.append([i, j])
    count = 0


    while q:
        x, y = q.popleft()
        if x == 0 and y == 7: return 1
        for i in range(9):
            nx = x+dx[i]; ny =y+dy[i]
            if not(0<=nx<8 and 0<=ny<8):
                continue
            if graph[nx][ny] == '.':
                if 0<=nx-1<8 and graph[nx-1][ny] == '.':
                    q.append([nx, ny])
        new_b = []
        #블록 이동
        for b1, b2 in block:
            graph[b1][b2] = '.'
            if 0<=b1+1<8:
                graph[b1+1][b2] = '#'
        block.clear()
        block = new_b
        count+=1
        if count == 9: return 1
    return 0
print(bfs())
'''