#스타트와 링크
n = int(input())
stats = [list(map(int, input().split())) for i in range(n)]
visited = [0] * n
ans = 99999

def is_it():
    global ans
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += stats[i][j]
            elif not visited[i] and not visited[j]:
                link += stats[i][j]
    ans = min(ans, abs(start - link))
    return

def resolve(iter):
    if iter == n:
        is_it()
        return
    visited[iter] = 1
    resolve(iter + 1)
    visited[iter] = 0
    resolve(iter + 1)
resolve(0)

print(ans)

'''
import itertools
import sys

n = int(sys.stdin.readline())
score = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr = [i for i in range(n)]
start = []
link = []
result = sys.maxsize
checknum = int(n/2)+1
if n%2 == 1:
    checknum == int(n/2)

for num in range(1, int(n/2)+1):
    a = sorted(list(itertools.combinations(arr, num)))

    for i in a:
        j = [x for x in arr if x not in i]
        #스타트팀
        for k in i:
            for l in i:
                if k != l:
                    start.append(score[k][l])
        #링크팀
        for k in j:
            for l in j:
                if k != l:
                    link.append(score[k][l])

        result = min(result, abs(sum(start)-sum(link)))
        start.clear()
        link.clear()

print(result)
'''