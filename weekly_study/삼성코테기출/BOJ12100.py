# 2048
from copy import deepcopy

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def move(board, dir):
    if dir == 0:  # 동쪽
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp

    elif dir == 1:  # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp

    elif dir == 2:  # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp

    else:
        for j in range(n): # 열
            top = 0
            for i in range(1, n): #행
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp

    return board


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)

ans = 0
dfs(graph, 0)
print(ans)

'''
import sys

input = sys.stdin.readline
n = int(input())

stage = [list(map(int, input().split())) for _ in range(n)]

result = []

def up(s):
    for i in range(n): # 열
        top = 0
        for j in range(1, n): #행
            if s[j][i]:
                temp = s[j][i]
                s[j][i] = 0
                if s[top][i] == 0: # 값 내리기
                    s[top][i] = temp
                elif s[top][i] == s[j][i]: # *2
                    s[top][i] = s[top][i]*2
                    top+=1
                else:
                    top+=1
                    s[top][i] = temp
    return s

print(up(stage))

def dfs(s, count):
    if count == 5: result.append(max(map(max, s))); return



'''