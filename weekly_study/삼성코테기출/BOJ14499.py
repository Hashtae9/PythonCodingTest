# 주사위 굴리기
from collections import deque

import sys
sys.setrecursionlimit(10**6)

N, M, y, x, k = map(int, input().split())
board = []

#지도의 숫자
for i in range(N):
    board.append(list(map(int, input().split())))

# 이동, 1:동 2:서 3:북 4:남
moving = list(map(int, input().split()))
mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

dice = [0, 0, 0, 0, 0, 0]

def dice_check(mn, f, e, b): #주사위 굴리기 전 후의 f, e, b 비교하여 규칙찾기
    if mn == 1: return f, 7-b, e #동
    elif mn == 2: return f, b, 7-e#서
    elif mn == 3: return b, e,7-f #남
    elif mn == 4: return 7-b, e, f #북

def dice_moving(dx, dy, mi, front, east, bottom): # mi : moving index
    if mi == k:
        return

    nx = dx+mx[moving[mi]-1]
    ny = dy+my[moving[mi]-1]

    if 0<=nx<M and 0<=ny<N:#범위 안
        value = board[ny][nx] # 움직였을때의 값

        #주사위는 3면이 결정되면 모양이 그려짐
        nf, ne, nb = dice_check(moving[mi], front, east, bottom)

        # board에 쓰여진 수가 0
        if value == 0: board[ny][nx] = dice[nb-1]
        else:
            dice[nb-1] = value
            board[ny][nx] = 0

        # 바닥의 반대편이 항상 출력됨
        print(dice[(7-nb)-1])
        dice_moving(nx, ny, mi+1, nf, ne, nb)

    else: #범위 밖
        dice_moving(dx, dy, mi+1, front, east, bottom)

    return
dice_moving(x, y, 0, 5, 3, 6)