# 차이를 최대로
import itertools
n = int(input())
arr = list(map(int, input().split()))
per = sorted(itertools.permutations(arr, n))

result = 0
for i in per:
    a = 0
    for j in range(len(i)):
        if j == len(i)-1:
            break
        a += abs(i[j]-i[j+1])
    result = max(a, result)
print(result)