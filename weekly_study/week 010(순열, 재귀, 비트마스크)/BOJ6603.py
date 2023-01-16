#로또
import itertools
while(True):
    a = list(map(int, input().split()))
    # 끝부분 확인
    if a[0] == 0:
        break

    per = sorted(list(itertools.combinations(a[1:], 6)))
    for i in per:
        print(*i)
    print()