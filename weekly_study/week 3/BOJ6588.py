#골드바흐 추측
from sys import stdin

array = [True for i in range(1000001)]

#범위가 1000000이므로 1001까지 범위로하면 1000000까지 범위가 커버됨
#해당 수의 배수들은 모두 소수가 아니므로 False로 변환
for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(stdin.readline())

    if n == 0: break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break
'''

import sys

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

prime_only = []

while True:
    a = int(sys.stdin.readline())

    if a == 0:
        exit()

    if prime_only:
        for i in range(prime_only[-1]+1, a+1):
            if isPrime(i):
                prime_only.append(i)
    else:
        for i in range(2, a+1):
            if isPrime(i):
                prime_only.append(i)

    for i in prime_only:
        if i>(int(a/2)+1):
            print("Goldbach's conjecture is wrong.")

        b = a-i
        if b in prime_only:
            print('{} = {} + {}'.format(a, i, b))
            break
'''