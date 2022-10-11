#골드바흐 파티션
import sys
t = int(sys.stdin.readline())

isPrime = [True]*1000001

isPrime[0] = isPrime[1] = False

for i in range(2, 1001):
    if isPrime[i]:
        for j in range(i+i, 1000001, i):
            isPrime[j] = False

for _ in range(t):
    a = int(sys.stdin.readline())
    count = 0
    for i in range(2, (a//2)+1):
        if isPrime[i] and isPrime[a-i]:
            count+=1
    print(count)