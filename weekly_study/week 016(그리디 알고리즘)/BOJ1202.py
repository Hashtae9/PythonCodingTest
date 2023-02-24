# 보석 도둑
import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().split())

gem_list = [list(map(int,input().split())) for _ in range(n)]
bag_list = [int(input()) for _ in range(k)]
gem_list.sort()
bag_list.sort()

result = 0
temp = []

#bag_list 가방이 담을 수 있는 무게 = i
for i in bag_list:
    # gem_list가 존재하고 가방이 담을 수 있는 무게가 보석의 무게와 같거나 클 때
    while gem_list and i>=gem_list[0][0]:
        # temp에 보석 가격 입력
        #- 를 붙여서 max heap 구현
        heapq.heappush(temp, -gem_list[0][1])
        heapq.heappop(gem_list)
    if temp: result -= heapq.heappop(temp) # temp에 요소가 있다면(가방에 들어간 보석이 있다면)
print(result)

'''
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

print(heapq)
print(bags)

answer = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(answer)
'''


'''
import sys

n, k = map(int, sys.stdin.readline().strip().split())
j = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] # 무게 가격
bag = [int(sys.stdin.readline()) for i in range(k)] # 각 가방별 무게
j.sort(key=lambda x:(-x[1], x[0]))
'''

