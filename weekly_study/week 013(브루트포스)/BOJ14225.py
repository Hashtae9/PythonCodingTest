# 부분수열의 합
import itertools
import sys

n = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))))
visited = [0]*2000001
visited[0] = 1

for i in range(1, n+1):
    com = list(itertools.combinations(num, i))
    for j in com:
        visited[sum(j)] = 1

print(visited.index(0))