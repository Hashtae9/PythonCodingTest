# 부등호
import itertools
k = int(input())
sign = list(input().split())
num = [i for i in range(10)]
s=[]
result = []
#sorted(list(itertools.permutations(num, k+1)))
per = sorted(list(itertools.permutations(num, k+1)))
for i in per:
    for j in range(k+1):
        if len(s) == k:
            s.append(i[-1])
            result.append(''.join(map(str, s)))
            s.clear()
            break

        if sign[j] == '>':
            if i[j] > i[j+1]:
                s.append(i[j])
            else:
                s.clear()
                break

        elif sign[j] == '<':
            if i[j] < i[j+1]:
                s.append(i[j])
            else:
                s.clear()
                break
print(result[-1])
print(result[0])