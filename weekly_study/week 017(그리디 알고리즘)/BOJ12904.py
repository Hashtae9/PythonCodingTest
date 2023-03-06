# a와 b
import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

for i in range(len(t)):
    if s == t: print(1); exit()
    if len(s) == len(t) and s != t: print(0); exit()

    if t[-1] == 'B':
        t.pop()
        t.reverse()
    elif t[-1] == 'A':
        t.pop()

'''
import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

def addA(arr):
    arr.pop()
    return arr

def reverseAndaddB(arr):
    arr.pop()
    for i in range(len(arr)):
        if arr[i] == 'A': arr[i] = 'B'
        elif arr[i] == 'B': arr[i] = 'A'
    return arr

# s 앞쪽부터 체크
for i in range(len(t)):
    if s == t: print(1); exit()
    if len(s) == len(t) and s != t: print(0); exit()

    if t[-1] == 'B': reverseAndaddB(t)
    elif t[-1] == 'A': addA(t)
'''