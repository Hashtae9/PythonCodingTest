#연결 요소의 개수
import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


# dfs로 그래프를 탐색한다.
def dfs(start, depth):

    #해당 노드 방문체크 한다.
    visited[start] = True

    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를탐색한다.
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs탐색을 돈다.
            count += 1  # 개수를 +1

print(count)

'''
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

print(count)
'''

'''
import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(idx, depth):
    visited[idx] =True
    for i in graph[idx]:
        if not visited[i]:
            dfs(i, depth+1)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]: # 1개일때는 dfs 돌리지말고 빠르게 처리하기
            count+=1
            visited[i] = True
        else:
            dfs(i, 0)
            count+=1
print(count)
'''