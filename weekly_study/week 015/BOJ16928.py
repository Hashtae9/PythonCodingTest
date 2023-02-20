# 뱀과 사다리 게임
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
moving_up = {}
moving_down = {}
for _ in range(n):
    before, after = map(int, sys.stdin.readline().strip().split())
    moving_up[before] = after
for _ in range(m):
    before, after = map(int, sys.stdin.readline().strip().split())
    moving_down[before] = after
visited = [-1]*101

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 0

    while q:
        start = q.popleft()
        for i in range(start+1, start+7):
            if i == 100:
                print(visited[start]+1)
                exit()

            if visited[i] == -1: #이전에 방문 x
                visited[i] = visited[start]+1
                if i in moving_up.keys():
                    if visited[moving_up[i]] == -1:
                        visited[moving_up[i]] = visited[i]
                        q.append(moving_up[i])
                elif i in moving_down.keys():
                    if visited[moving_down[i]] == -1:
                        visited[moving_down[i]] = visited[i]
                        q.append(moving_down[i])
                else:
                    q.append(i)

bfs()