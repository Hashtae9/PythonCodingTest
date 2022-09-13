#덱 (10866번)
import sys

n = int(sys.stdin.readline())

deque = []
for _ in range(n):
    str = sys.stdin.readline().split()
    if str[0] == 'push_front':
        list=[]
        list.append(str[1])
        deque = list+deque

    if str[0] == 'push_back':
        deque.append(str[1])

    if str[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print("-1")
    if str[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print("-1")
    if str[0] == 'size':
        print(len(deque))
    if str[0] == 'empty':
        if deque:
            print("0")
        else :
            print("1")
    if str[0] == 'front':
        if deque:
            print(deque[0])
        else :
            print("-1")
    if str[0] == 'back':
        if deque:
            print(deque[-1])
        else :
            print("-1")