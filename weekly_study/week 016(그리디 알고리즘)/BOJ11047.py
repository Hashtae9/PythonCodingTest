# 동전 0
import sys

n, k = map(int, sys.stdin.readline().split())
count = 0
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

for i in coin[::-1]:
    if i>k: continue
    count += k//i
    k = k%i

print(count)