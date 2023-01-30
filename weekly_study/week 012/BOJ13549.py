#숨바꼭질 3
from collections import deque

n, k = map(int, input().split())  # n: 수빈이가 있는 위치, k: 동생이 있는 위치
q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == -1:
        visited[s-1] = visited[s] + 1
        q.append(s-1)
    if 0 < s*2 < 100001 and visited[s*2] == -1:
        visited[s*2] = visited[s]
        q.appendleft(s*2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        visited[s+1] = visited[s] + 1
        q.append(s+1)

'''
import sys
from collections import deque
sys.setrecursionlimit(100000)

n, k = map(int, input().split())
dist = [-1 for i in range(100001)]
q = deque()
q.append(n)
dist[n] = 0

while q:
    a = q.popleft() #a는 현 위치, b는 방문여부
    if a == k:
        print(dist[a])
        break

    for nt in (a-1, a+1):
        if 0<= nt <= 100000 and dist[nt] == -1:
            dist[nt] = dist[a] + 1
            q.append(nt)

    if 0<= a*2 <= 100000 and dist[a*2] == -1:
        dist[a*2] = dist[a]
        q.appendleft(a*2)
'''