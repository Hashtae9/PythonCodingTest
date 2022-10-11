import sys
nge_size = int(sys.stdin.readline())

nge = list(map(int, sys.stdin.readline().split()))
# nge = [9, 5, 4, 8]

result = [-1]*nge_size
stack = []

# stack에 인덱스를 넣어준다.
# nge[stack[-1]]과 다음 값을 비교해서 다음 값이 작으면 stack에 인덱스 추가
# 다음값이 크면 stack에 저장된 인덱스 값 pop하면서 해당 값의 result값 다음값으로 변경

for i in range(nge_size):
    while stack and nge[stack[-1]] < nge[i]:
        result[stack.pop()] = nge[i]
    stack.append(i)

# asterisk unpacking
print(*result)
