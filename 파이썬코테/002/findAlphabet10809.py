import sys
from string import ascii_lowercase

n = list(sys.stdin.readline().strip())

for i in ascii_lowercase:
    if i not in n:
        print(-1, end=' ')
    else:
        print(n.index(i), end=' ')