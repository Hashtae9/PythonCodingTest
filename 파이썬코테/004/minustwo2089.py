import sys
import math
n = int(sys.stdin.readline())

result = []
if n == 0:
    print('0')
    exit()
while n != 1:
    result.append(n - (-2*math.ceil(n/-2)))
    n = math.ceil(n/-2)    
result.append(1)
# print(''.join(str(s) for s in result[::-1]))
for i in result[::-1]:
    print(i, end='')