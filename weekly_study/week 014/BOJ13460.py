# 13460 구슬 탈출2
from collections import deque
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
s = []
def move(i, j, dx, dy):
    c = 0
    while s[i + dx][j + dy] != "#" and s[i][j] != "O":
        i += dx
        j += dy
        c += 1
    return i, j, c
def bfs():
    while q:
        ri, rj, bi, bj, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            if s[nbi][nbj] != "O":
                if s[nri][nrj] == "O":
                    print(d)
                    return
                if nri == nbi and nrj == nbj:
                    if rc > bc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visit[nri][nrj][nbi][nbj]:
                    visit[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, d + 1])
    print(-1)
for i in range(n):
    a = list(input())
    s.append(a)
    for j in range(m):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j
q = deque()
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj] = True
bfs()


'''
import sys
from copy import deepcopy
n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

def up(board, cnt):
    global limit
    for i in range(m):  # 세로 한줄 선택
        pointer = n-1
        rp = -1
        bp = -1
        for j in range(n-2, -1, -1):
            if board[j][i] != '#':
                if board[j][i] == 'R':
                    rp = j
                elif board[j][i] == 'B':
                    bp = j
                elif board[j][i] == 'O': #구멍이 있는 경우
                    if bp == -1 and rp != -1: limit = min(limit, cnt)

            elif board[j][i] == '#':
                if rp != -1 and bp != -1: #빨간공 파란공 둘다 해당행에 있음
                    board[bp][i] = '.'
                    board[rp][i] = '.'
                    if bp > rp: # 빨간공이 더 위에 있는 경우
                        board[pointer][i] = 'R'
                        board[pointer+1][i] = 'B'
                    else:
                        board[pointer][i] = 'B'
                        board[pointer+1][i] = 'R'
                    bp = -1; rp = -1
                else: #둘중 하나만 있거나 하나도 없는 경우
                    if rp != -1:
                        board[rp][i] = '.'
                        board[pointer][i]='R'
                        rp = -1
                    elif bp != -1:
                        board[bp][i] = '.'
                        board[pointer][i]='B'
                        bp = -1
            pointer = j
    return board

def down(board, cnt):
    global limit
    for i in range(m):  # 세로 한줄 선택
        pointer = 1
        rp = -1
        bp = -1
        for j in range(1, n):
            if board[j][i] != '#':
                if board[j][i] == 'R':
                    rp = j
                elif board[j][i] == 'B':
                    bp = j
                elif board[j][i] == 'O': #구멍이 있는 경우
                    if bp == -1 and rp != -1: limit = min(limit, cnt)

            elif board[j][i] == '#':
                if rp != -1 and bp != -1: #빨간공 파란공 둘다 해당행에 있음
                    board[bp][i] = '.'
                    board[rp][i] = '.'
                    if bp > rp: # 빨간공이 더 위에 있는 경우
                        board[pointer-1][i] = 'R'
                        board[pointer][i] = 'B'
                    else:
                        board[pointer-1][i] = 'B'
                        board[pointer][i] = 'R'
                    bp = -1; rp = -1
                else: #둘중 하나만 있거나 하나도 없는 경우
                    if rp != -1:
                        board[rp][i] = '.'
                        board[pointer][i]='R'
                        rp = -1
                    elif bp != -1:
                        board[bp][i] = '.'
                        board[pointer][i]='B'
                        bp = -1
            pointer = j
    return board

def left(board, cnt):
    global limit
    for i in range(1, n-1):  # 가로 한줄 선택
        pointer = m-2
        rp = -1
        bp = -1
        for j in range(m-1, -1, -1):
            if board[i][j] != '#':
                if board[i][j] == 'R':
                    rp = j
                elif board[i][j] == 'B':
                    bp = j
                elif board[i][j] == 'O': #구멍이 있는 경우
                    if bp == -1 and rp != -1: limit = min(limit, cnt)

            elif board[i][j] == '#':
                if rp != -1 and bp != -1: #빨간공 파란공 둘다 해당행에 있음
                    board[i][bp] = '.'
                    board[i][rp] = '.'
                    if bp > rp: # 빨간공이 더 왼쪽에 있는 경우
                        board[i][pointer] = 'R'
                        board[i][pointer+1] = 'B'
                    else:
                        board[i][pointer] = 'B'
                        board[i][pointer+1] = 'R'
                    bp = -1; rp = -1
                else: #둘중 하나만 있거나 하나도 없는 경우
                    if rp != -1:
                        board[i][rp] = '.'
                        board[i][pointer]='R'
                        rp = -1
                    elif bp != -1:
                        board[i][bp] = '.'
                        board[i][pointer]='B'
                        bp = -1
            pointer = j
    return board

def right(board, cnt):
    global limit
    for i in range(1, n-1):  # 가로 한줄 선택
        pointer = 1
        rp = -1
        bp = -1
        for j in range(1, m):
            if board[i][j] != '#':
                if board[i][j] == 'R':
                    rp = j
                elif board[i][j] == 'B':
                    bp = j
                elif board[i][j] == 'O': #구멍이 있는 경우
                    if bp == -1 and rp != -1: limit = min(limit, cnt)

            elif board[i][j] == '#':
                if rp != -1 and bp != -1: #빨간공 파란공 둘다 해당행에 있음
                    board[i][bp] = '.'
                    board[i][rp] = '.'
                    if bp < rp: # 빨간공이 더 오른쪽에 있는 경우
                        board[i][pointer] = 'R'
                        board[i][pointer-1] = 'B'
                    else:
                        board[i][pointer] = 'B'
                        board[i][pointer-1] = 'R'
                    bp = -1; rp = -1
                else: #둘중 하나만 있거나 하나도 없는 경우
                    if rp != -1:
                        board[i][rp] = '.'
                        board[i][pointer]='R'
                        rp = -1
                    elif bp != -1:
                        board[i][bp] = '.'
                        board[i][pointer]='B'
                        bp = -1
            pointer = j
    return board

limit = 10
def dfs(board, cnt):
    global result
    if cnt >= limit:
        # 2차원 배열 요소 중 가장 큰 값 반환
        return
    dfs(up(deepcopy(board), cnt), cnt + 1)
    dfs(down(deepcopy(board), cnt), cnt + 1)
    dfs(left(deepcopy(board), cnt), cnt + 1)
    dfs(right(deepcopy(board), cnt), cnt + 1)
dfs(graph, 1)

if limit == 10: print(-1)
else: print(limit)
#5 5
#####
#BR.#
#.#.#
#.O.#
#####'''