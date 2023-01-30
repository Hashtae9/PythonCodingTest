# 서울 지하철 2호선
# 순환찾기 = dfs, 거리 찾기 = bfs
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


'''
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1) ]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)
isCycle = [False]*(n+1)
check = [-1]*n
cycle = False

def dfs(cur, start, cnt):
    global cycle
    if cnt >= 2 and cur == start:
        cycle = True
        return

    visited[cur] = True # 역 방문
    for i in graph[cur]: # 다음 방문 역 고르기
        if not visited[i]: # 방문하지 않는 경우 dfs
            dfs(i, start, cnt+1)
        elif i == start and cnt>=2: # 다음역이 이미 방문한 곳
            dfs(i, start, cnt) # 역을 2개 이상 걸쳤는데 다음역이 시작역과 같은경우

def bfs():
    global check
    queue = deque()
    for i in range(n):
        if isCycle[i]:
            check[i] = 0
            queue.append(i)

    while len(queue) !=0:
        cur = queue.popleft()
        for n in graph[cur]: # 현재 역과 연결되어 있는 역중 다음 역 선택
            if check[n] == -1: # 한번도 방문한적 없는 역
                queue.append(n)
                check[n] = check[cur] + 1

    for i in check:
        print()

'''