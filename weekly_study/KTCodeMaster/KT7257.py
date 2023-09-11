# 영화제

import copy
import sys
from itertools import permutations

n = int(sys.stdin.readline())
score = []
for i in range(n):
    score.append(list(map(int, sys.stdin.readline().split())))

def sort_and_count(score, a, b, c):
    score.sort(key=lambda x:(-x[a], -x[b], -x[c]))

    for index, value in enumerate(score):
        delete_count = 0

        sscore = copy.deepcopy(score)[index:]
        # 중복 문제 해결
        sscore.remove(value)
        sscore.sort(key=lambda x:(x[b], x[c]))
        for second_value in sscore:
            if delete_count == 2: break

            if (second_value[1] <= value[1]) and (second_value[2] <= value[2]) and (second_value[0] <= value[0]):
                score.remove(second_value)
                delete_count+=1

    return len(score)

num_list = [0, 1, 2]
result = []
for i, j, k in list(permutations(num_list)):
    copy_score = copy.deepcopy(score)
    result.append(sort_and_count(copy_score, i, j, k))

print(min(result))