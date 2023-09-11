# 친척수
import sys

n = int(sys.stdin.readline())
num = []
result = [1]
for i in range(n):
    num.append(int(sys.stdin.readline()))

for i in range(2, max(num)):
    a = num[0] % i
    for j in range(1, n):
        if num[j] % i != a:
            break
        if j == len(num)-1 and num[j]%i == a:
            result.append(i)

print(*result)