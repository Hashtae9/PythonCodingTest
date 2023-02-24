# 동전 뒤집기
n = int(input())
coin = [list(input()) for _ in range(n)]
ans = n * n + 1

for bit in range(1 << n):
    tmp = [coin[i][:] for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'

    tot = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T':
                cnt += 1
        tot += min(cnt, n-cnt)
    ans = min(ans, tot)

print(ans)



'''
import copy
import sys

n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for i in range(n)]
board1 = copy.deepcopy(board)

chechnum = int(n/2) if n%2==0 else int((n+1)/2)

def filp_raw(arr, i):
    for j in range(n):
        if arr[i][j] == 'H' : arr[i][j] = 'T'
        else: arr[i][j] = 'H'

def flip_column(arr, i):
    for j in range(n):
        if arr[j][i] == 'H' : arr[j][i] = 'T'
        else: arr[j][i] = 'H'

#행 => 열 순 뒤집기
for i in range(n):
    count = 0
    for j in range(n):
        if board1[i][j] == 'T': count+=1
    if count >= chechnum:
        filp_raw(board1, i)
for i in range(n):
    count = 0
    for j in range(n):
        if board1[j][i] == 'T': count+=1
    if count >= chechnum:
        flip_column(board1, i)

#열 => 행 순 뒤집기
for i in range(n):
    count = 0
    for j in range(n):
        if board[j][i] == 'T': count+=1
    if count >= chechnum:
        flip_column(board, i)
for i in range(n):
    count = 0
    for j in range(n):
        if board[i][j] == 'T': count+=1
    if count >= chechnum:
        filp_raw(board, i)

cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'T': cnt1+=1
        if board1[i][j] == 'T': cnt2+=1
print(min(cnt1, cnt2))
'''