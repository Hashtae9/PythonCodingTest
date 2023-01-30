# 코테 파이썬 정리집(트리, bfs&dfs)

## bfs & dfs

### bfs, dfs에서 왼쪽, 오른쪽, 위, 아래로 움직여야 하는 경우

```
import sys

n,m=map(int,input().split())
game=[[p for p in sys.stdin.readline().strip()] for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

ans=False
def dfs(x,y,cnt,color,sx,sy):
    global ans

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        #사이클을 하나 찾으면 종료시키기
        if ans is True:
            return
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        #최소한의 사이클인 4이상이면서 첫번째좌표와 현재좌표가 같으면 True
        if cnt>=4 and sx==nx and sy==ny:
            ans=True
            return True
        if visited[nx][ny]==0 and game[nx][ny]==color:
            visited[nx][ny]=1
            dfs(nx,ny,cnt+1,color,sx,sy)
            visited[nx][ny]=0
    return False


def solve():
    global ans
    for i in range(n):
        for j in range(m):
            sx=i
            sy=j
            visited[sx][sy]=True
            dfs(i,j,1,game[i][j],sx,sy)
            if ans:
                return 'Yes'
    return 'No'
print(solve())
```

 ### dfs, bfs가 둘 다 사용되는 경우

```
# 16947번 서울 지하철 2호선

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 순환선이 존재하는지 확인하는 함수
def circulation_station(start, idx, cnt):
    global cycle
    # 방문한 역이 2곳 이상이고, 현재 역이 시작 역으로 돌아온다면
    if start == idx and cnt >= 2:
        # 순환선으로 표시
        cycle = True
        return
    # 현재 역 방문 표시
    visited[idx] = True
    # 다음 방문할 역을 받으면서
    for i in info[idx]:
        # 아직 방문하지 않은 역이라면
        if not visited[i]:
            # 해당 역을 추가하고 재귀적으로 호출
            circulation_station(start, i, cnt + 1)
        # 이미 방문한 역이며 방문한 역이 2곳 이상이라면
        elif i == start and cnt >= 2:
            # 방문하는 역을 그대로 재귀적 호출
            circulation_station(start, i, cnt)

# 역과 순환역 사이의 거리를 확인하는 함수
def distance_station():
    global check
    q = deque()
    # 순환역에 속하는 역은 모두 거리가 0
    for i in range(n):
        if cycle_station[i]:
            check[i] = 0
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 현재 역
        now = q.popleft()
        # 다음 역 선택
        for i in info[now]:
            # 역이 순환선에 포함되지 않는 역이라면
            if check[i] == -1:
            	# 큐에 추가
                q.append(i)
                # 이동 거리 구하기
                check[i] = check[now] + 1
    # 모든 각 역과 순환선 사이의 최소 거리 출력
    for i in check:
        print(i, end=' ')

# 역의 개수 입력받기
n = int(input())
# 역과 역을 연결하는 구간의 정보
info = [[] for _ in range(n)]
# 순환역을 표시하는 전체 역
cycle_station = [False] * n
# 정답 변수
check = [-1] * n

# 역 구간 정보 입력받기
for _ in range(n):
    a, b = map(int, input().split())
    info[a-1].append(b-1)
    info[b-1].append(a-1)

# 순환선 확인
for i in range(n):
    # 방문 여부 표시 리스트
    visited = [False] * n
    # 순환선이 있는지 여부
    cycle = False
    # 순환선 탐색
    circulation_station(i, i, 0)
    # 순환선이 있다면 순환선에 속하는 역을 순환역으로 표시
    if cycle:
        cycle_station[i] = True

# 역 거리 확인
distance_station()
```



### bfs에서 연산 우선순위 증가를 위해 appendleft()사용하기

```
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


# BFS 벽을 최소 몇 개 부수어야 하는가?
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]  # 가중치

q = deque()
q.append((0,0))
dist[0][0] = 0
while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if arr[nx][ny] == 0: #미로값 == 0
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
print(dist[n-1][m-1])
```





### dfs를 주로 쓰는 경우

+ 순환 찾기



### bfs를 주로 쓰는 경우

+ 최소 횟수 찾기



## 트리

```
import sys
n = int(sys.stdin.readline().strip())
tree = {} #딕셔너리 사용 key, value형태 이용

#트리에 값 집어 넣기
for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0]) # left 왼쪽먼저 쭉 출력
        preorder(tree[root][1]) # right 왼쪽 후 오른쪽 출력

def inorder(root):
    if root != '.':
        inorder(tree[root][0]) #왼쪽먼저 쭉 들어가서 root 출력
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root !='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
```



```
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
```

