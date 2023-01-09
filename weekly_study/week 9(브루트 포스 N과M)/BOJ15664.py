# n과 m 10
import itertools

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result=[]
a = sorted(list(set(itertools.combinations(arr, m))))
for i in a:
    print(*i)

#*연산자 = 배열앞에 붙여서 print에 사용시 여러개의 인자를 넘긴 효과
# [1, 2, 3] => 1 2 3

'''
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s=[]
result = []
def dfs(start):
    if len(s) == m:
        result.append(' '.join(map(str, s)))
        return
    for i in range(start, n):
        s.append(arr[i])
        dfs(i+1)
        s.pop()
dfs(0)
print('\n'.join(sorted(list(set(result)))))
'''