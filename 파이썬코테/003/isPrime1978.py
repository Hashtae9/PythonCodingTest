import sys
n = int(sys.stdin.readline())

result = 0

a = list(map(int, sys.stdin.readline().split()))
# a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
for i in a:
    isPrime = True
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            isPrime = False
            break
    if not isPrime:
        continue
    result += 1

print(result)