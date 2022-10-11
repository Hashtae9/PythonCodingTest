#최소공배수
import math

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(math.lcm(a, b))