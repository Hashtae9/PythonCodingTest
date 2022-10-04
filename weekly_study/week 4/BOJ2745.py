# 진법 변환
import sys

n, b = sys.stdin.readline().rstrip().split()
print(int(n, int(b)))