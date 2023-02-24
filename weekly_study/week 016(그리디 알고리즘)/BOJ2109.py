# 순회 강연
import sys
import heapq

n = int(sys.stdin.readline())
md = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
md.sort(key = lambda x:(x[1]))
p_list=[]
for i in md:
    heapq.heappush(p_list, i[0])
    if (len(p_list)>i[1]):
        heapq.heappop(p_list)

print(sum(p_list))
