# 나이트의 이동
from collections import deque
import sys
sys.setrecursionlimit(5000)

n = int(input())
dx = [1, 2, 1, 2, -1, -2, -1, -2]
dy = [2, 1, -2, -1, 2, 1, -2, -1]
for _ in range(n):
    l = int(input())
    my = list(map(int, input().split()))
    want = list(map(int, input().split()))
    chess = [[0]*l for i in range(l)]
    visited = [[False]*l for i in range(l)]
    def dfs():
        queue = deque()
        queue.append(my)
        while queue:
            x, y = queue.popleft()
            if x == want[0] and y == want[1]:
                print(chess[x][y]); return
            if 0<=x<l and 0<=y<l and visited[x][y] == False:
                visited[x][y] = True
                for k in range(8):
                    if 0<=x+dx[k]<l and 0<=y+dy[k]<l:
                        queue.append([x+dx[k], y+dy[k]])
                        chess[x+dx[k]][y+dy[k]] = chess[x][y]+1
    dfs()

'''
1
100
0 0
30 50
'''