# 가장 가까운 두 점

import sys
n = int(input())

# n개의 점을 입력 받아 2차원 리스트로 저장
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort()  # x좌표를 기준으로 정렬


def get_dist(a, b):  # 두 점 사이의 거리를 구하는 함수
    return (a[0]-b[0])**2+(a[1]-b[1])**2


def get_min(start, end):
    if start == end:  # 점이 하나인 경우, 최대값 반환
        return sys.maxsize

    if end - start == 1:  # 점이 두 개인 경우, 두 점 사이의 거리 반환
        return get_dist(arr[start], arr[end])

    mid = (start + end) // 2  # 중간 지점 계산
    # 왼쪽 절반과 오른쪽 절반을 각각 재귀적으로 호출하여 최소 거리를 구함
    min_dist = min(get_min(start, mid), get_min(mid, end))

    # 가운데 점(mid)을 기준으로 거리가 min_dist보다 작은 점들을 candidates 리스트에 추가
    candidates = []
    for i in range(start, end+1):
        if (arr[mid][0] - arr[i][0])**2 < min_dist:
            candidates.append(arr[i])

    # candidates 리스트를 y좌표를 기준으로 정렬
    candidates.sort(key=lambda x: x[1])

    # candidates 리스트 내에서 최소 거리를 구함
    for i in range(len(candidates)-1):
        for j in range(i+1, len(candidates)):
            # y좌표 차이가 min_dist보다 작은 경우에만 최소 거리 계산
            if (candidates[i][1] - candidates[j][1])**2 < min_dist:
                min_dist = min(min_dist, get_dist(
                    candidates[i], candidates[j]))
            else:
                break

    return min_dist


print(get_min(0, n-1))

''' 메모리 초과 => why?
import heapq
import sys
import math
from itertools import combinations

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
com = list(combinations(arr, 2))
result = []
for d1, d2 in com:
    distance = abs(d1[0]-d2[0]) + abs(d1[1]-d2[1])
    heapq.heappush(result, (distance, d1, d2))

dis, r1, r2 = heapq.heappop(result)
result = (r1[0]-r2[0])**2+(r1[1]-r2[1])**2
print(result)
'''