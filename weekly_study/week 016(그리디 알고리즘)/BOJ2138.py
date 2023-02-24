# 전구와 스위치
n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))


def change(A, B):
    L = A[:]
    press = 0
    for i in range(1, n):
        # 이전 전구가 같은 상태면 pass
        if L[i-1] == B[i-1]:
            continue
        # 상태가 다를 경우
        press += 1
        for j in range(i-1, i+2):
            if j<n:
                L[j] = 1 - L[j]
    return press if L == B else 1e9


# 첫번째 전구의 스위치를 누르지 않는 경우
res = change(bulb, target)
# 첫번째 전구의 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb, target) + 1)
print(res if res != 1e9 else -1)

'''
import copy
import sys

n = int(sys.stdin.readline())

start = list(map(int, sys.stdin.readline().strip()))
end = list(map(int, sys.stdin.readline().strip()))
count = 0
def flip(arr, i):
    for a in (i-1, i, i+1):
        if a == -1: continue
        if a == n: continue
        arr[a] = 1 - arr[a]

# 첫번째를 누르고 시작한 경우
s1 = copy.deepcopy(start)
flip(s1, 0)
for i in range(1, n):
    flip(s1, i)
    count+=1
    if s1 == end: print(count); exit()
count = 0
# 첫번째를 안누르고 시작한 경우
for i in range(1, n):
    flip(start, i)
    count+=1
    if start == end: print(count); exit()

print(-1)
'''
