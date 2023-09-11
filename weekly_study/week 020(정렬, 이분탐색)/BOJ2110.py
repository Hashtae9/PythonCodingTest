# 공유기 설치
import sys

n, c = map(int, sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

start = 1
end = house[-1] - house[0]
answer = 0
while start <= end:
    mid = (start+end)//2
    current = house[0] #시작
    count = 1

    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)