import sys
from collections import Counter

nge_size = int(sys.stdin.readline())

nge = list(map(int, sys.stdin.readline().split()))
# nge = [9, 5, 4, 8]

nge_counter = Counter(nge)

stack = []
result = [-1]*nge_size

for i in range(nge_size):
    while stack and nge_counter[nge[stack[-1]]] < nge_counter[nge[i]]:
        result[stack.pop()] = nge[i]
    stack.append(i)
    
print(*result)