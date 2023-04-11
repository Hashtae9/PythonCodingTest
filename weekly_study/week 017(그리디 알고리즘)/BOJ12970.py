# AB
def solution():
    n,k = map(int,input().split())

    a = 0
    b = n
    while a*b < k and b > 0:
        a += 1
        b -= 1

    # 10 12
    # 2 8

    if k == 0:
        return 'B'*n
    elif b == 0:
        return -1

    remain = k - (a-1)*b

    return 'A'*(a-1) + 'B'*(b-remain) + 'A' + 'B'*remain

print(solution())

'''
import math
n, k = map(int, input().split())

# 011
# 10
# 1001101001
# bbbaaabbbb
# 1 12 2 6 3 4
# 6 13
#  ab

for b_count in range(1, math.cail(n/2)):
    if k%b_count == 0:
        a_count = int(k/b_count)
        if a_count+b_count <=n:
'''
