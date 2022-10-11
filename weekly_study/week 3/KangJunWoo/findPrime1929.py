

# for i in range(a,b+1):
#     isPrime = True
#     if i == 1:
#         continue
#     for j in range(2,i):
#         if i%j == 0:
#             isPrime = False
#             break
#     if not isPrime:
#         continue
#     num_prime.append(i) 

# for i in num_prime:
#     print(i)
import sys
a, b = map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print(i)

# 분기처리 for-else문
# https://studymake.tistory.com/208