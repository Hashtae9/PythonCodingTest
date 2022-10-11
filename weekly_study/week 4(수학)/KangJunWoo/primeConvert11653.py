import sys
n = int(sys.stdin.readline())
if n == 1:
    exit()

prime = [False, False] + [True]*10000000

for i in range(2, 3163):
    if prime[i]:
        for j in range(i+i, 10000002, i):
            prime[j] = False
result = []
for i in range(2,10000000):
    if n == 1:
        break
    if prime[n]:
        result.append(n)
        break
    if not prime[i]:
        continue
    else:
        if n%i == 0:
            while n%i == 0:
                n = int(n/i)
                result.append(i)
        
for i in result:
    print(i)
            