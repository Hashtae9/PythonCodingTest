#숨바꼭질 4
import sys
from collections import deque
sys.setrecursionlimit(100000)
n, k = map(int, input().split())
level = [0 for _ in range(100001)]
before = [-1 for _ in range(100001)]
count = 0
def bfs():
    q = deque()
    q.append(n)
    #before[n] = n #시작점

    while q:
        a = q.popleft()
        if a == k:
            print(level[a])
            count = level[a]
            break

        for nt in (a-1, a+1, a*2):
            if 0 <= nt <= 100000 and not level[nt]:
                q.append(nt)
                level[nt] = level[a]+1
                before[nt] = a
bfs()
log = []
q2 = deque()
q2.append(k)
while q2:
    num = q2.popleft()
    log.append(num)
    if num == n:
        break
    q2.append(before[num])
log.reverse()
print(*log)