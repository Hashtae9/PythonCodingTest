# 대회 or 인턴
import sys

n, m, k = map(int, sys.stdin.readline().strip().split())

charge = 0
for i in range(m, -1, -1):
    if n-k+charge >= i*2: print(i); break
    else:
        if charge<k: charge+=1
