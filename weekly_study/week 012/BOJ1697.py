# 숨바꼭질
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dist = [0]*100001
# n 은 +-1 or n*2 이동
q = deque()
q.append(N)
while q:
    a = q.popleft()
    count = 0
    if a == K:
        print(dist[a])
        exit()

    for nt in (a-1, a+1, a*2):
        if 0 <= nt < 100001 and not dist[nt]:
            dist[nt] = dist[a]+1
            q.append(nt)
