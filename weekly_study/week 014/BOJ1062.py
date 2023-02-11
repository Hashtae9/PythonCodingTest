# 가르침
import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1


def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)
print(answer)

'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = []
dic = {'a', 'n', 't', 'i', 'c'}
for _ in range(n):
    a = sys.stdin.readline().strip()
    b = a[4:len(a)-4]
    for i in ['a', 'n', 't', 'i', 'c']:
        b = b.replace(i, '')
    graph.append(b)
    for i in b:
        dic.add(i)
# a n t i c
print(dic)
graph.sort(key=len)
print(graph)

if k < 5: print(0); exit()

def bfs():
    q =deque()
    q.append(graph[0])
    count = k-5

    while q:
        if count == 0:
            c = 0
            for i in graph:
                if i == '':
                    c+=1
            print(c)
            exit()

        a = q.popleft()
        if a not in dic:
            dic.add(a)
            count-=1
            for i in range(len(graph)):
                if a in graph[i]:
                    graph[i] = graph[i].replace(a, '')
            graph.sort(key=len)
            for i in graph:
                if i != '': q.append(i); break

bfs()'''