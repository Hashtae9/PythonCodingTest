# atm
import sys

n = map(int, sys.stdin.readline())
time = list(map(int, sys.stdin.readline().strip().split()))

time.sort()
result = 0
add = 0
for i in time:
    result = result + i+add
    add = add+i

print(result)