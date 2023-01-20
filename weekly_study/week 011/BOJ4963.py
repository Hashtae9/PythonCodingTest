# 섬의 개수
'''
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    field[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    field = []
    count = 0
    for _ in range(h):
        field.append(list(map(int, read().split())))
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
'''

'''
from collections import deque
import sys
read = sys.stdin.readline

def bfs(x, y):
  dx = [1, -1, 0, 0, 1, -1, 1, -1]
  dy = [0, 0, -1, 1, -1, 1, 1, -1]
  field[x][y] = 0
  q = deque()
  q.append([x, y])
  while q:
    a, b = q.popleft()
    for i in range(8):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
        field[nx][ny] = 0
        q.append([nx, ny])

while True:
  w, h = map(int, read().split())
  if w == 0 and h == 0:
    break
  field = []
  count = 0
  for _ in range(h):
    field.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        bfs(i, j)
        count += 1
  print(count)
'''


def dfs(y,x):
    # 범위 벗어나는 경우 건너뛰기
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    # 바다인경우 건너뛰기
    # if graph[x][y]==0:
    #     return False

    # 섬인경우 재귀
    if graph[y][x] == 1:
        #방문처리
        graph[y][x] = 0
        # 상하좌우 탐색
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        # 대각선 탐색
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        return True
    return False


while True:
    w,h = map(int,input().split())

    if w == 0 & h ==0 :
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result += 1
    print(result)
