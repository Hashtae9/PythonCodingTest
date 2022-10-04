# -2진수
#음수일때는 몫이 소수점이고 나머지가 있다면 + 1
# -13 = -2*7 + 1
# 7 = -2*-3 + 1
# -3 = -2*2 + 1
# 2 = -2*-1 + 0
# -1 = -2*1 + 1
# 1 = -2*0 + 1
#110111

# 2진수
# 14 = 2*7 + 0
# 7 = 2*3 + 1
# 3 = 2*1 + 1
# 1 = 2*0 + 1
# 1110

import sys

n = int(sys.stdin.readline())

if not n:
    print('0')
    exit()

result = ''
while n:
    n
    if n%-2:
        n = n//-2 + 1
        result = '1' + result
    else:
        n = n//-2
        result = '0' + result
print(result)