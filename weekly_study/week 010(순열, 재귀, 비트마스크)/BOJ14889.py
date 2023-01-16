#스타트와 링크
import itertools
import sys

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
arr = [i for i in range(n)]
start = []
link = []
result = sys.maxsize

a = sorted(list(itertools.combinations(arr, int(n/2))))

for i in a[:(int(len(a)/2))]:
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
