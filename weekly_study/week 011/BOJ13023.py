#ABCDE
n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False]*n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

s=[]
result = 0

def dfs(idx, num):
    if num == 4:
        print(1)
        exit()

    for i in graph[idx]: # idx와 연결된 사람중 visited 한적 있는지 없는지 체크
        if not visited[i]:
            visited[i] = True
            dfs(i, num+1)
            visited[i] = False

# 노드를 순서대로 방문하며 dfs를 수행합니다.
for i in range(n):
    visited[i] = True # i에 연결된 친구가 4개이상인지 체크해보기
    dfs(i, 0)
    visited[i] = False # 아니라면 다시 false

print(0)