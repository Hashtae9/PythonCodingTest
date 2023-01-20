# DFS BFS
from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)  # dfs의 방문기록
visited2 = [False] * (N + 1)  # bfs의 방문기록


def bfs(V):
    q = deque([V])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
    visited2[V] = True  # 해당 V 값을 방문처리
    while q:  # q가 빌때까지 돈다.
        V = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
        print(V, end=" ")  # 해당 값 출력
        for i in range(1, N + 1):  # 1부터 N까지 돈다
            if not visited2[i] and graph[V][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                visited2[i] = True  # i 값을 방문처리


def dfs(V):
    visited1[V] = True  # 해당 V값 방문처리
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited1[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)


dfs(V)
print()
bfs(V)

'''
n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
s1=[v]
def dfs(idx):
    if len(s1) == n:
        print(*s1)
        bfs(v)

    for i in graph[idx]:
        if i not in s1:
            s1.append(i)
            dfs(i)
            s1.pop()

s2=[v]
def bfs(idx):
    if len(s2) == n:
        print(*s2)
        exit()

    for i in range(1, len(graph[idx])+1):
        if graph[idx][i] not in s1:
            s2.append(graph[idx][i])

            if i == len(graph[idx]):
                bfs(graph[idx][1])

dfs(v)
'''