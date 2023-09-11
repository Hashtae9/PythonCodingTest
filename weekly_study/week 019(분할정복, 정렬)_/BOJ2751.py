# 수 정렬하기
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr = list(set(arr))
arr.sort(key = lambda x:x)
for i in range(n):
    print(arr[i])