
def convert(n):
    return chr(n+55)
import sys
m, n = map(int, sys.stdin.readline().split())

result = []
while m != 0:
    result.append(m%n)
    m = m//n

for i in result[::-1]:
    if i >= 10:
        print(convert(i), end='')
    else:
        print(i, end='')
