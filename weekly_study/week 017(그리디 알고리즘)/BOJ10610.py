# 30
# 3의 배수는 각 자리수의 합이 3의 배수여야 가능
n = input()

if "0" not in n:
    print(-1)

else:
    num_sum = 0
    for i in range(len(n)):
        num_sum += int(n[i])

    if num_sum % 3 != 0:
        print(-1)

    else:
        sorted_num = sorted(n, reverse=True)
        answer = "".join(sorted_num)
        print(answer)

'''
import itertools
import sys

num = list(map(int, list(sys.stdin.readline().strip())))
num.sort(key=lambda x : -x)

if 0 not in num: print(-1); exit()
num.pper = list(itertools.permutations(num, i))op()

for i in range(len(num), 0, -1):
    
    for j in per:
        a = int(''.join(map(str, j)))
        if a%3==0: print(a*10); exit()

print(-1)
'''