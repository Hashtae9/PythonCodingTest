import sys
from string import ascii_lowercase

n = list(sys.stdin.readline().strip())

alphabet_dict = {}

for i in ascii_lowercase:
    alphabet_dict[i] = 0

for i in n:
    alphabet_dict[i] += 1

for i in ascii_lowercase:
    print(alphabet_dict[i], end=' ')

# arr=input()
# cnt=[0]*26

# for i in arr:
#     cnt[ord(i)-97]+=1

# print(*cnt)

