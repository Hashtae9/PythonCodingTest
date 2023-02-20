# 스도미노쿠
def go(cnt, itr):
    find = False
    if cnt == Ecnt:
        print('Puzzle', itr)
        for r in range(9):
            for c in range(9):
                print(A[r][c], end='')
            print()
        return True
    r, c = E[cnt]
    if A[r][c]:
        find = go(cnt + 1, itr)
        return find
    for i in range(9):
        for j in range(9):
            if i == j or Visit[i][j]:
                continue
            for d in dr:
                pair_x, pair_y = r + d[0], c + d[1]
                if 0 <= pair_x <= 8 and 0 <= pair_y <= 8 and not A[pair_x][pair_y]:
                    if R[r][i] == R[pair_x][j] == C[c][i] == C[pair_y][j] == S[r // 3 * 3 + c // 3][i] == S[pair_x // 3 * 3 + pair_y // 3][j] == 0:
                        A[r][c], A[pair_x][pair_y] = i + 1, j + 1
                        Visit[i][j], Visit[j][i] = 1, 1
                        R[r][i], R[pair_x][j], C[c][i], C[pair_y][j], S[r // 3 * 3 + c // 3][i], S[
                            pair_x // 3 * 3 + pair_y // 3][j] = 1, 1, 1, 1, 1, 1
                        find = go(cnt + 1, itr)
                        if find:
                            return find
                        A[r][c], A[pair_x][pair_y] = 0, 0
                        Visit[i][j], Visit[j][i] = 0, 0
                        R[r][i], R[pair_x][j], C[c][i], C[pair_y][j], S[r // 3 * 3 + c // 3][i], S[
                            pair_x // 3 * 3 + pair_y // 3][j] = 0, 0, 0, 0, 0, 0
    return find


itr = 1
while True:
    N = int(input())
    dr = [[0, 1], [1, 0]]

    if N == 0:
        break
    A = [[0] * 9 for _ in range(9)]
    Visit = [[0] * 9 for _ in range(9)]
    R = [[0] * 9 for _ in range(9)]
    C = [[0] * 9 for _ in range(9)]
    S = [[0] * 9 for _ in range(9)]
    E = []
    Ecnt = 0
    for _ in range(N):
        U, LU, V, LV = input().split()
        U_x, U_y = ord(LU[0]) - ord('A'), int(LU[1]) - 1
        V_x, V_y = ord(LV[0]) - ord('A'), int(LV[1]) - 1
        A[U_x][U_y], A[V_x][V_y] = int(U), int(V)
        Visit[int(U) - 1][int(V) - 1], Visit[int(V) - 1][int(U) - 1] = 1, 1
        R[U_x][int(U) - 1], R[V_x][int(V) - 1] = 1, 1
        C[U_y][int(U) - 1], C[V_y][int(V) - 1] = 1, 1
        S[U_x // 3 * 3 + U_y // 3][int(U) - 1] = 1
        S[V_x // 3 * 3 + V_y // 3][int(V) - 1] = 1
    for i, pos in enumerate(input().split()):
        pos_x, pos_y = ord(pos[0]) - ord('A'), int(pos[1]) - 1
        A[pos_x][pos_y] = i + 1
        R[pos_x][i], C[pos_y][i] = 1, 1
        S[pos_x // 3 * 3 + pos_y // 3][i] = 1
    for r in range(9):
        for c in range(9):
            if not A[r][c]:
                E.append([r, c])
                Ecnt += 1
    go(0, itr)
    itr += 1
'''
#
import itertools
from collections import deque
import sys
sys.setrecursionlimit(20000)
dic = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5,
       'G' : 6, 'H' : 7, 'I' : 8}
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 1

while True:
    n = int(input())
    if n == 0: break
    sdoku = [[0]*9 for _ in range(9)]
    com = list(itertools.combinations(num, 2))
    addnum = 0

    for _ in range(n):
        num1, num1_loc, num2, num2_loc = input().split()
        sdoku[dic[num1_loc[0]]][int(num1_loc[1]) - 1] = int(num1)
        sdoku[dic[num2_loc[0]]][int(num2_loc[1]) - 1] = int(num2)
        if (int(num1), int(num2)) in com:
            com.remove((int(num1), int(num2)))
        elif (int(num2), int(num1)) in com:
            com.remove((int(num2), int(num1)))
        addnum += 2

    a = list(input().split())
    for i in range(1, 9+1):
        sdoku[dic[(a[i-1])[0]]][int((a[i-1])[1]) - 1] = i
    addnum += 9

    blank = deque()
    for i in range(9):
        for j in range(9):
            if sdoku[i][j] == 0:
                blank.append((i, j))

    #여기까지가 스토쿠 입력값 받아오기

    def checkRow(x, a):
        for i in range(9):
            if a == sdoku[x][i]:
                return False
        return True

    def checkCol(y, a):
        for i in range(9):
            if a == sdoku[i][y]:
                return False
        return True

    def checkRect(x, y, a):
        nx = x // 3 * 3
        ny = y // 3 * 3
        for i in range(3):
            for j in range(3):
                if a == sdoku[nx+i][ny+j]:
                    return False
        return True

    def check_x_plus(x, y, a, b, idx):
        if checkRow(x, a) and checkCol(y, a) and checkRect(x, y, a) \
                and checkRow(x+1, b) and checkCol(y, b) and checkRect(x+1, y, b):
            sdoku[x][y] = a
            sdoku[x+1][y] = b
            index1 = blank.index((x+1,y))
            blank.remove((x+1, y))
            dfs(idx+2)
            blank.appendleft((x+1, y))
            sdoku[x][y] = 0
            sdoku[x+1][y] = 0
            blank.insert(index1, (x+1, y))

        if checkRow(x, b) and checkCol(y, b) and checkRect(x, y, b) \
                and checkRow(x+1, a) and checkCol(y, a) and checkRect(x+1, y, a):
            sdoku[x][y] = b
            sdoku[x+1][y] = a
            index2 = blank.index((x+1,y))
            blank.remove((x+1, y))
            dfs(idx+2)
            blank.appendleft((x+1, y))
            sdoku[x][y] = 0
            sdoku[x+1][y] = 0
            blank.insert(index2, (x+1, y))

    def check_y_plus(x, y, a, b, idx):
        if checkRow(x, a) and checkCol(y, a) and checkRect(x, y, a) \
                and checkRow(x, b) and checkCol(y+1, b) and checkRect(x, y+1, b):
            sdoku[x][y] = a
            sdoku[x][y+1] = b
            index3 = blank.index((x,y+1))
            blank.remove((x, y+1))
            dfs(idx+2)
            sdoku[x][y] = 0
            sdoku[x][y+1] = 0
            blank.insert(index3, (x, y+1))

        if checkRow(x, b) and checkCol(y, b) and checkRect(x, y, b) \
                and checkRow(x, a) and checkCol(y+1, a) and checkRect(x, y+1, a):
            sdoku[x][y] = b
            sdoku[x][y+1] = a
            index4 = blank.index((x,y+1))
            blank.remove((x, y+1))
            dfs(idx+2)
            sdoku[x][y] = 0
            sdoku[x][y+1] = 0
            blank.insert(index4, (x, y+1))

    def dfs(idx):
        global count
        if idx == 81:
            for i in range(9):
                print(*sdoku[i])
            return


        for a, b in com:
            if blank:
                x, y = blank.popleft()
                if x != 8 and sdoku[x+1][y] == 0 :
                    com.remove((a, b))
                    check_x_plus(x, y, a, b, idx)
                    com.append((a, b))
                if y != 8 and sdoku[x][y+1] == 0:
                    com.remove((a, b))
                    check_y_plus(x, y, a, b, idx)
                    com.append((a, b))
                blank.appendleft((x, y))

    dfs(addnum)'''