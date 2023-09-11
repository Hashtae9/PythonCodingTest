# 랜선 자르기
import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan) #이분탐색 처음과 끝위치

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in lan:
        lines += i // mid #분할 된 랜선 수

    if lines >= N: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)



# k, n = map(int, input().split())
#
# line = []
# for _ in range(k):
#     line.append(int(input()))
#
# q = sum(line)//n
#
# for i in range(min(q, min(line)), 0, -1):
#     result = 0
#     for j in line:
#         result += j//i
#     if result == n:
#         print(i)
#         exit()