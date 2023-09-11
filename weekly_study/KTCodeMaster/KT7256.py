# 조삼모사
# import sys
#
# n = int(sys.stdin.readline())
# dotori = list(map(int, sys.stdin.readline().split()))
# given = int(sys.stdin.readline())
#
# a = sum(dotori)
# if a<=given: # 도토리 원하는 양보다 주어진 양이 더 많을때
#     print(max(dotori))
# else:
#     while a > given:
#         result = [i for i in dotori if i != max(dotori)]
#         for i in range(n-len(result)):
#             result.append(max(result))
#         dotori = result
#         a = sum(dotori)
#     print(max(dotori))
import sys

n = int(sys.stdin.readline())
dotori = list(map(int, sys.stdin.readline().split()))
given = int(sys.stdin.readline())
def ebun(d, g):
    left, right = 1, max(d)
    result = 0

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for i in d:
            count+=min(i, mid)

        if count<=g:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


# 최대 도토리 개수 출력
print(ebun(dotori, given))

