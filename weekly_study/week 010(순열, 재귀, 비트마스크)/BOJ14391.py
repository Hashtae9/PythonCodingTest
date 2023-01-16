# 종이 조각
def bitmask():
    global maxAns
    # 비트마스크로 2^(N*M)의 경우의 수를 따져본다
    for i in range(1 << n * m):
        total = 0
        # 가로 합 계산
        for row in range(n):
            rowsum = 0
            for col in range(m):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미
                idx = row * m + col
                # 가로일때
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                # 세로일때 앞에서 나온 수를 total에 더하고 rowsum 초기화
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # 세로 합 계산
        for col in range(m):
            colsum = 0
            for row in range(n):
                # idx 는 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미
                idx = row * m + col
                # 세로일때
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                # 가로일때 앞에서 나온 수를 total에 더하고 colsum 초기화
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        maxAns = max(maxAns, total)


n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

maxAns = 0
bitmask()
print(maxAns)

'''
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

if n < m:
    s = 0
    for i in range(n):
        s += int(''.join(map(str, arr[i])))
        if i == n-1: break
    print(s)

elif n > m:
    s = 0
    trans_arr = list(map(list, zip(*arr)))
    for i in range(m):
        s += int(''.join(map(str, trans_arr[i])))
        if i == m-1: break
    print(s)

else: # n == m
    s1 = 0
    s2 = 0
    trans_arr = list(map(list, zip(*arr)))
    for i in range(n):
        s1 += int(''.join(map(str, arr[i])))
        s2 += int(''.join(map(str, trans_arr[i])))
        if i == n-1: break
    print(max(s1, s2))
'''