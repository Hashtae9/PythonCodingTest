# 카드

import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = dict()
for i in range(n):
    a = int(sys.stdin.readline())
    if a not in arr.keys():
        arr[a] = 1
    else:
        arr[a] += 1

result = sorted(arr.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])