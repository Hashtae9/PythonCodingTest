# 종이의 개수
import sys
input = sys.stdin.readline

n = int(input())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

papers = []
for _ in range(n):
    row = list(map(int, input().rsplit()))
    papers.append(row)


def check(row, col, n):
    global minus_cnt, zero_cnt, plus_cnt
    curr = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n)  # 1
                check(row, col + next_n, next_n)  # 2
                check(row, col + (2 * next_n), next_n)  # 3
                check(row + next_n, col, next_n)  # 4
                check(row + next_n, col + next_n, next_n)  # 5
                check(row + next_n, col + (2 * next_n), next_n)  # 6
                check(row + (2 * next_n), col, next_n)  # 7
                check(row + (2 * next_n), col + next_n, next_n)  # 8
                check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
                return

    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1
    return


check(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)

'''
import sys

input = sys.stdin.readline
n = int(input())
num = [list(map(int, input().split())) for _ in range(9)]
visited = [[0]*9 for _ in range(9)]

a = 0
b = 0
c = 0

def check_num(arr, x, y, length):
    check = arr[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if arr[i][j] != check: return 2
    return check

d = n
while d != 1:
    for i in range(0, n-1, d//3 if d//3 != 0 else 1):
        for j in range(0, n-1, d//3 if d//3 != 0 else 1):
            if visited[i][j] == 1: continue
            elif visited[i][j] == 0:
                check = check_num(num, i, j, d//3 if d//3 != 0 else 1)
                if check == 2: continue
                else:
                    for x in range(i, i+ (d//3 if d//3 != 0 else 1)):
                        for y in range(j, i+ (d//3 if d//3 != 0 else 1)):
                            visited[x][y] = 1
                    if check == -1: a+=1
                    elif check == 0: b+=1
                    elif check == 1: c+=1
    d = d//3


print(a)
print(b)
print(c)
'''