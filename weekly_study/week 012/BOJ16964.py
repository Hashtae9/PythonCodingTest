# DFS 스페셜 저지
# https://vixxcode.tistory.com/29
import sys
N = int(sys.stdin.readline())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
ans= list(map(int,sys.stdin.readline().split()))
level=[False]*(N+1)
tsize = [0]*(N+1)
visited = [False]*(N+1)

def dfs(x,lv):
    if visited[x]:
        return 0
    visited[x]=True
    size=1
    level[x]=lv
    for i in range(len(graph[x])):
        next =graph[x][i]
        size+=dfs(next,lv+1)
    tsize[x]=size
    return size


if ans[0]!=1:
    print("0")
    sys.exit(0)
else:
    dfs(1,0)
    for i in range(1,N):
        x=ans[i]
        if tsize[x] == 1 or i + tsize[x] >=N:
            continue
        next = ans[i+tsize[x]]
        if level[next]>level[x]:
            print(0)
            sys.exit(0)
    print(1)

'''
import sys
input = sys.stdin.readline

start = 1 # 시작점
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
children = [set() for _ in range(N+1)] # 트리의 부모자식 관계를 알기 위함
for _ in range(N-1): # 그래프 생성
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
test_case = list(map(int,input().split())) # 비교할 탐색 루트

def dfs(idx):
    if visited[idx]: return

    visited[idx] =True

    for i in graph[idx]:
        if visited[i] == False:
            children[idx].add(i)
            dfs(i)

dfs(test_case[0])
visited = [0 for _ in range(N+1)]
visited[test_case[0]] = 1
for i in range(1, len(test_case)):
    if children[test_case[i-1]]: #자식이 있다면
        #print(test_case[i])
        #print(children[test_case[i-1]])
        #print(test_case[i] in children[test_case[i-1]])
        if test_case[i] not in children[test_case[i-1]] or visited[test_case[i]] == 1: # 자식에 test_case가 없고 방문한적도 없다면
            print(0); exit()
    visited[test_case[i]] = 1
print(1)
'''

