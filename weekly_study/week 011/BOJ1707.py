# 이분 그래프
import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


def dfs(start, group):
    global error

    # 만약 사이클이 true라면 재귀탈출
    if error:
        return

    visited[start] = group  # 해당 그룹으로 등록

    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정
        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면
            error = True  # 에러값 True
            return  # 그후 재귀 리턴

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크
    error = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:  # 만약 아직 방문하지 않았다면
            dfs(i, 1)  # dfs를 돈다.
            if error:  # 만약 에러가 참이라면
                break  # 탈출

    if error:
        print('NO')
    else:
        print('YES')

'''
import sys
k = int(sys.stdin.readline())
check = True
def dfs(gra, root, rb, log):
    global check
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in log:
            log.append(n)
            if visited[n] == 0:
                visited[n] = rb
                rb = rb*(-1)
                for j in gra[n]:
                    if j in log: continue
                    stack += [j]
    if len(log)%2 == 1:
        if visited[log[0]] != visited[log[-1]]:
            check = False
    if len(log)%2 == 0:
        if visited[log[0]] == visited[log[-1]]:
            check = False

for _ in range(k):
    v, e = map(int, input().split())
    visited = [0]*(v+1)
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        dfs(graph, i, 1)
        if not check: print('NO'); break
    print('YES')
'''
