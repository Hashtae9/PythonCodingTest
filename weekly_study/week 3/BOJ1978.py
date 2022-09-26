# 소수찾기
n = int(input())
data = list(map(int, input().split()))
count = 0

for x in data:
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                count += 1

            break

print(count)


'''
n = int(input())

num = list(map(int, input().split()))

count = 0

for n in num:
    if n == 1:
        break
    for i in range(2, n + 1):
        if n % i == 0:
            if n == i:
                count += 1

            break

print(count)
'''