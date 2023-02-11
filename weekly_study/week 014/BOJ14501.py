#퇴사
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0

def get_score(day, score):
    global result
    d, s = graph[day]
    if day+d >= n:
        if day+d == n: result = max(score+s, result); return
        result = max(score, result); return

    for i in range(day+d, n):
        get_score(i, score+s)

for i in range(n): # 첫 시작 날짜
    get_score(i, 0)

print(result)