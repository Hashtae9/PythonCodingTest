import sys
t = int(sys.stdin.readline())

for i in range(t):
    gcd = 0
    a, b = map(int, sys.stdin.readline().split())
    lcm = a*b
    while b != 0:
        a, b = b, a%b
    gcd = a
    lcm = lcm/a
    print(int(lcm))

