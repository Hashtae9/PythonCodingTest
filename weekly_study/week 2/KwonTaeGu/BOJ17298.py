#오큰수(17298번)

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []

#오큰수가 없을경우 -1이 나오기 떄문에 기본값을 -1로 초기화
answer = [-1 for i in range(n)]

#오른쪽수가 왼쪽 수보다 작을때는 그냥 index를 기록하면서 계속 진행하다가 오른쪽수가 더 큰 케이스가 나오면
#이전까지 저장한 index들을 전부다 점검(왜냐하면 stack에 기록됬다는 것은 내림차순으로 정리가 되어있다는 뜻)
for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)

#꿀팁인데, 파이썬에서 배열을 print할 때, 앞에 *을 붙여주면 공백을 기준으로 원소들만 나열된다.


'''
# 시간 복잡도가 2중 for문이라서 실패(시간초과)
import sys

def NGE(index, numbers):
    a = int(numbers[index])
    for i in numbers[index+1:]:
        if a < int(i):
            return i
    return -1

n = int(sys.stdin.readline())
num = list(sys.stdin.readline().split())

ans = []

for i in range(len(num)):
    ans.append(str(NGE(i, num)))

print(" ".join(ans))
'''

