# 다리 만들기
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
distance = [[-1] * N for _ in range(N)]     # 거리 리스트
sea = deque([])     # 육지 가장자리 x, y 좌표와 육지 번호 저장


# 육지 넘버링
def numbering(board, number):
    q = deque([])
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                board[i][j] = number
                distance[i][j] = 0  # 육지라서 거리 0 (다리가 아니기 때문)

                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr = r + dir[d][0]
                        nc = c + dir[d][1]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                            # 육지라면 넘버링 계속 진행
                            if board[nr][nc] == 1:
                                q.append((nr, nc))
                                visited[nr][nc] = True
                                board[nr][nc] = number  # 넘버링 진행
                                distance[nr][nc] = 0

                            # 육지의 상하좌우 중 하나가 바다라면 (가장자리라는 말과 같음)
                            # 육지의 가장자리 좌표와 육지 번호 저장
                            elif board[nr][nc] == 0:
                                sea.append((r, c, number))
                                # 실수로 (nr, nc, number)를 저장했음.
                                # ★ 다음 좌표가 아닌 현재 좌표 (r, c, number)를 저장해야함.

                number += 1


# 다리 놓기
def extend(board):
    answer = 1e9
    while sea:
        r, c, bridge = sea.popleft()
        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if 0 <= nr < N and 0 <= nc < N:
                # 바다라면 다리를 놓아준다.
                if board[nr][nc] == 0:
                    # 육지번호가 bridge 인 육지에서 다리를 설치한다는 뜻
                    board[nr][nc] = bridge
                    distance[nr][nc] = distance[r][c] + 1   # 다리길이 + 1
                    sea.append((nr, nc, bridge))

                # 다른 육지에서 놓은 다리와 만날경우 거리 계산
                # 즉, 섬과 섬이 이어졌다는 뜻
                elif board[nr][nc] != bridge:
                    answer = min(answer, distance[r][c] + distance[nr][nc])
                    # flag 변수를 만들어서 강제로 while 문 종료시켜도 될 듯하다.
                    # --> 섬과 섬을 잇는 최초의 다리는 가장 짧은 다리이기 때문이다.

    return answer


numbering(board, 1)
print(extend(board))

'''
import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 섬을 1이 아닌 타 숫자로 다 표현하기
def check_land(x, y, ln):
    if land[x][y] == 1:
        land[x][y] = ln
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<N:
                check_land(x+dx[i], y+dy[i], ln)
        return

land_num = 2
for i in range(N):
    for j in range(N):
        if land[i][j] == 1:
            check_land(i, j, land_num)
            land_num+=1

result = sys.maxsize

def find_bridge(x, y, land_number,count):
    global result
    if count == (N*2)-3:
        return

    for t in range(4):
        if 0<=x+dx[t]<N and 0<=y+dy[t]<N:
            if land[x+dx[t]][y+dy[t]] == 0:
                find_bridge(x+dx[t], y+dy[t], land_number, count+1)
            elif land[x+dx[t]][y+dy[t]] != land_number: #기존 섬이 아닌 다른 섬 도착
                result = min(result, count); return
    return

for k in range(N):
    for l in range(N):
        if land[k][l] != 0:
            find_bridge(k, l, land[k][l], 0)

print(result)
'''