#이전 순열
n = int(input())
result = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if result[i-1]>result[i]:
        for j in range(n-1, 0, -1):
            if result[i-1] > result[j]:
                result[i-1], result[j] = result[j], result[i-1]
                result = result[:i] + sorted(result[i:])[::-1]
                print(*result)
                exit()
print(-1)

'''
12345
12354
12435
12453
12534
12543
13245
13254
13425
13452
'''