#나이순 정렬
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = sys.stdin.readline().split()
    arr.append([i, int(a), b])
arr.sort(key=lambda x:(x[1], x[0]))
for j in arr:
    print("{} {}".format(j[1], j[2]))