import sys
nge_size = int(sys.stdin.readline())

nge = list(map(int, sys.stdin.readline().split()))
# nge = [9, 5, 4, 8]

i = 0

will_print = []
# nge 수열에 대하여 
while i < len(nge):
    std = nge[i]
    j = i + 1
    while j < len(nge):
        if std < nge[j]:
            will_print.append(nge[j])
            break
        else:
            j += 1
    if j == len(nge):
        will_print.append(-1)
    i += 1 
for i in will_print:
    print(i, end=' ')

# 입력된 수열 하나하나씩에 대하여
# 오른쪽 수열이 지금 수열보다 크면 바로 오른쪽수열 출력 후 다음 수열로
# 오른쪽 수열이 지금보다 작으면 다음 오른쪽 수열로
# 수열이 끝까지 가면 -1
