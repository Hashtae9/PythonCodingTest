#오등큰수(17299)

import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
count = Counter(arr) # 변수 마다 개수를 저장
result = [-1] * n
stack.append(0)

for i in range(n):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)

'''

def count(list):
    num_max = max(list)
    list_return = [0]*(num_max+1)
    for i in range(num_max+1):
        a = list.count(i)
        list_return.insert(i, a)
    return list_return

list_a = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 8, 8, 8, 8]
print(count(list_a))

#[0, 4, 3, 2, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''