def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

import sys
n, m = map(int, sys.stdin.readline().split())

factorial_n = factorial(n)
factorial_m = factorial(m)
minus_nm = factorial(n-m)
temp = int(factorial_n/factorial_m/minus_nm)
combi = list(str(temp))[::-1]

result = 0
for i in combi:
    if i != '0':
        break
    else:
        result += 1
print(result)
