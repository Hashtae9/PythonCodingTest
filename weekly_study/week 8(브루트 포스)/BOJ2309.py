#일곱 난쟁이
import itertools

'''
s = []
for i in range(9):
    s.append(int(input()))
'''
array = [int(input()) for i in range(9)]

com = itertools.combinations(array, 7)

for seven in com:
    if sum(seven) == 100:
        for i in sorted(seven):
            print(i)
        break #찾으면 바로 나가줘야함(안나가면 조합수가 너무 많아 틀렸다고 함)