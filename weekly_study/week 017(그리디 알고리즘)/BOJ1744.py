# 수 묶기
# n : 데이터의 크기
n = int(input())

# plus : 양수 데이터 리스트, minus : 음수 데이터 리스트
plus = []
minus = []

result = 0
for i in range(n):
    num = int(input())
    if num > 1: #1을 포함하면 안됨
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

# 정렬
plus.sort(reverse=True)
minus.sort() # ex) -3 -2 -1

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)

'''
import sys

n = int(sys.stdin.readline())
plus = []
minus = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num<=0: minus.append(num)
    else : plus.append(num)

plus.sort(key=lambda x : -x)
minus.sort()

aws = 0

for i in range(0, len(minus), 2):
    if i+1>=len(minus): aws+=minus[i]
    else: aws+=(minus[i]*minus[i+1])

for i in range(0, len(plus), 2):
    if i+1>=len(plus): aws+=plus[i]
    else: aws += (plus[i]*plus[i+1])
print(aws)
'''