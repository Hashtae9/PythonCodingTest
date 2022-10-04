def gcd(a, b):
    while b != 0:
        a, b = b, a%b

    return a

import sys
n = int(sys.stdin.readline())

for i in range(n):
    result = 0
    strn = sys.stdin.readline().split()
    num_input = int(strn[0])
    for i in range(1, num_input+1):
        for j in range(i+1, num_input+1):
            result += gcd(int(strn[i]),int(strn[j]))
    print(result)
