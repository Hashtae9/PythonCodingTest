#영양
import sys
from itertools import combinations

n = int(sys.stdin.readline())
num = [i for i in range(n)]
score = []

for _ in range(n):
    score.append(list(map(int, sys.stdin.readline().split())))
com = list(combinations(num, int(n//2)))
result = []
for i in com[:int(len(com)//2)]:
    other_element = []
    for k in num:
        if k not in i: # 반대쪽 싸이드
            other_element.append(k)
    a_side = 0
    b_side = 0
    for x, y in list(combinations(i, 2)):
        a_side += score[x][y] + score[y][x]

    for x,y in list(combinations(other_element, 2)):
        b_side += score[x][y] + score[y][x]
    result.append(abs(a_side-b_side))

print(min(result))