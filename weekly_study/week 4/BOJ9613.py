#GCD합
import sys
from itertools import combinations
import math

n = int(sys.stdin.readline())

set = {}

for _ in range(n):
    num = sys.stdin.readline().split()[1:]
    result = 0
    comb = combinations(num[:], 2)
    for a, b in comb:
        result += math.gcd(int(a), int(b))
    print(result)