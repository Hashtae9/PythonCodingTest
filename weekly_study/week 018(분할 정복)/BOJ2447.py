# 별 찍기 10
import sys
sys.setrecursionlimit(10**6)

def paint_star(LEN):
    DIV3 = LEN//3
    if LEN == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*']*3
        return

    paint_star(DIV3)

    for i in range(0, LEN, DIV3):
        for j in range(0, LEN, DIV3):
            if i != DIV3 or j != DIV3:
                for k in range(DIV3):
                    g[i+k][j:j+DIV3] = g[k][:DIV3]

n = int(sys.stdin.readline().strip())
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()

'''
import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

star = [['*' for _ in range(n)] for i in range(n)]

def make_blank(x, y, length):
    a = length//3
    if a == 0: return

    for i in range(x, length, a if a != 0 else 1):
        for j in range(y, length, a if a != 0 else 1):
            if ((a if a != 0 else 1) <= i < 2*(a if a != 0 else 1)) & ((a if a != 0 else 1) <= j < 2*(a if a != 0 else 1)):
                star[i][j] = ' '
            else: make_blank(i, j, length//3)

make_blank(0, 0, n)
for k in star:
    print(*k)
'''