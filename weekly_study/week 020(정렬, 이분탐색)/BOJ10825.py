# 국영수
import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a = sys.stdin.readline().split()
    arr.append([a[0], int(a[1]), int(a[2]), int(a[3])])

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(arr[i][0])