# 외판원 순회 2
import sys

n = int(input())
arr = [i for i in range(n)]
price = [list(map(int, input().split())) for _ in range(n)]
res = sys.maxsize
def dfs(start, next, value, visited): # 시작번호 다음번호 합 개수
    global res
    if len(visited) == n:
        if price[next][start] != 0:
            res = min(res, value + price[next][start])
        return

    for i in range(n):
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if price[next][i] != 0 and i not in visited and value < res:
            visited.append(i) #그 도시를 방문목록에 추가
            dfs(start, i, value + price[next][i], visited) #그 도시를 방문한다.
            visited.pop() #방문을 완료했다면 방문목록 해제
#도시마다(0~3) 출발점을 지정
for i in range(n):
    dfs(i, i, 0, [i])

print(res)

''' 시간초과
import itertools

n = int(input())
arr = [i for i in range(n)]
per = sorted(list(itertools.permutations(arr, n)))

price = []
result = 0
for _ in range(n):
    k = list(map(int, input().split()))
    result += sum(k)
    price.append(k)

for p in per:
    a = 0
    for i in range(len(p)):
        if i == len(p)-1:
            a += price[p[i]][p[0]]
            break
        a += price[p[i]][p[i+1]]
    result = min(result, a)

print(result)
'''

'''
  0 1 2 3 0
0     15
1 5
2       12
3   8
'''