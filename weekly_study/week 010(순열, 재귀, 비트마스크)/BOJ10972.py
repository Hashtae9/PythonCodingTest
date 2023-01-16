#다음 순열
n = int(input())
result = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    #앞열의 값 < 뒷열의 값
    if result[i-1] < result[i]:
        for j in range(n-1, 0, -1): # 위의 result[i-1]과 어느열을 바꿔야 할지 비교
            if result[i-1] < result[j]:
                result[i-1], result[j] = result[j], result[i-1]
                result = result[:i] + sorted(result[i:])
                print(*result)
                exit()
print(-1)

'''
1234
1243
1324
1342
1423
1432

'''


# 메모리 초과
'''
import itertools

n = int(input())
arr = [i for i in range(1, n+1)]
result = tuple(map(int, input().split()))
per = sorted(list(itertools.permutations(arr, n)))
for i in range(len(per)):
    if per[i] == result:
        if per[i] == per[-1]:
            print(-1)
            break
        print(*per[i+1])
        break
'''