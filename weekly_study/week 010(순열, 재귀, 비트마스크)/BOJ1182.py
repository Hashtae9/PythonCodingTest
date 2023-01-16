#부분 수열의 합
import itertools

n, s = map(int, input().split())
arr = list(map(int, input().split()))
result=0
for i in range(1, n+1):
    com = sorted(itertools.combinations(arr, i))
    for j in com:
        if sum(j) == s:
            result+=1
print(result)