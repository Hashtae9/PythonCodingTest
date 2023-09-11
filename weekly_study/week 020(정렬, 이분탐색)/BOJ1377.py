# 버블 소트
import sys

n = int(input())
arr = []
for i in range(n):
    arr.append( [int(sys.stdin.readline()), i] )

st = sorted(arr)
result = []

for i in range(n):
    result.append(st[i][1] - arr[i][1])

print(max(result) + 1)
