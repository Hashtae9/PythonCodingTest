#소인수 분해
import sys
n = int(sys.stdin.readline())
count = 2
while n!=1:
    if n%count == 0:
        print(count)
        n //=count
    else:
        count+=1