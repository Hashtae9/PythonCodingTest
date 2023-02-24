# 회의실 배정
import sys

n = int(sys.stdin.readline())
check = [[0]*2 for _ in range(n)]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    check[i][0]=a #시작시간
    check[i][1]=b #끝시간
check.sort(key=lambda x: (x[1], x[0]))

count = 1

end_time = check[0][1]
for i in range(1, n):
    if check[i][0] >= end_time:
        count+=1
        end_time = check[i][1]
print(count)