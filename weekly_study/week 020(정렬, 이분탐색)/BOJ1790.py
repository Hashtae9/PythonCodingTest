# 수 이어 쓰기2

n, k = map(int, input().split())
ans = 0
digit = 1
nine = 9


while k > digit*nine:
    k = k-(digit * nine)
    ans = ans + nine
    digit+=1
    nine = nine*10

ans = (ans+1) + (k-1) // digit

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])

# import sys
#
# N, k = map(int, sys.stdin.readline().split())
# # 0 ~ 8 123456789 => 9개 = 9 * 1
# # 9 ~ 188  1011121314151617181920212223... 2개씩 => 180 개 9 * 20
# # 189 ~    100 101 102 103 ... 3개씩 => 9 * 300
#
# # 23 9*1보다 큼 => 23 - 9 = 14
# # 14 = 2*7 + 0
#
# # 25 24-9 = 15
# # 15 = 2*7 + 1
#
# default = 1
# zari = 1
# while k >= default * 9:
#     k -= default * 9
#     default *= 10
#     zari += 1
#
# q = (k-1) // zari
# r = (k-1) % zari
# result = default + q
# if result > N:
#     print(-1)
# else:
#     print(str(result)[r])