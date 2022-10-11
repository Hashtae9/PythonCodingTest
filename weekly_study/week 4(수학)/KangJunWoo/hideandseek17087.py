def gcd(a, b):
    while b != 0:
        a, b = b, a%b

    return a

import sys
n, s = map(int, sys.stdin.readline().split())

position = list(map(int, sys.stdin.readline().split()))
position_diff = []
for i in position:
    position_diff.append(abs(i - s))
distance = min(position_diff)
for i in position_diff:
    distance = gcd(distance, i)

print(distance)