# 배열 합치기
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(*sorted(arr1+arr2))