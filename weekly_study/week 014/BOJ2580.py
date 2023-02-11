#스도쿠
import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)

'''
sdoku = [list(map(int, input().split())) for _ in range(9)]
zero = []

def checknum(x, y, i):
    if i not in sdoku[x] and i not in [t[y] for t in sdoku]:
        rx = (x//3)*3
        ry = (y//3)*3
        check = []
        for k in range(rx, rx+3):
            for l in range(ry, ry+3):
                check.append(sdoku[k][l])
        if i not in check:
            return i
    return 0

def findnum(arr):
    if len(arr) == 0:
        for i in range(9):
            print(*sdoku[i])
        exit()

    a, b = arr.pop()
    for i in range(1, 9+1):
        r = checknum(a, b, i)
        if r != 0:
            sdoku[a][b] = r
            findnum(arr)
            sdoku[a][b] = 0

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zero.append([i, j])

findnum(zero)
'''