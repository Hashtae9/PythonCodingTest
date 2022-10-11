#네 수
import sys
num = list(map(str, sys.stdin.readline().split()))
a = num[0] + num[1]
b = num[2] + num[3]

result = int(a) + int(b)
print(result)