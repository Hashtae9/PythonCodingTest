# 4연산
import sys
from collections import deque

input = sys.stdin.readline
s, t = map(int, input().split())
queue = deque()
check = set()
queue.append((s,''))
check.add(s)
MAX = 10e9

if s == t:
    print(0)
else:
    res = -1
    while queue:
        c_v, c_s = queue.popleft()
        if c_v == t:
            res = c_s
            print(res)
            exit(0)

        n_v = c_v * c_v
        if 0 <= n_v <= MAX and n_v not in check:
            queue.append((n_v, c_s+'*'))
            check.add(n_v)

        n_v = c_v + c_v
        if 0 <= n_v <= MAX and n_v not in check:
            queue.append((n_v, c_s+'+'))
            check.add(n_v)

        n_v = 1
        if n_v not in check:
            queue.append((n_v, c_s+'/'))
            check.add(n_v)
    print(res)

'''
import collections
import sys

s, t = map(int, sys.stdin.readline().strip().split())

if s == t:
    print(0)
    exit()

def bfs(start, end):
    q = collections.deque()
    q.append(start)
    visited = set()
    box = ['*', '+', '-', '/']
    while q:
        a = q.popleft()
        if visited[a] == '': continue
        if a == end: return visited[a]

        for i in range(4):
            if i == 4:
                if a != 0:
                    new_a = 1
                    visited[new_a] = visited[a] + box[i]
            else:
                new_a = eval(str(a)+box[i]+str(a))
                visited[new_a] = visited[a] + box[i]
    return -1

a = bfs(s, t)
print(a)
'''