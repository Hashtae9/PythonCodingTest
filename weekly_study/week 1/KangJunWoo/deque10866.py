import sys
a = int(sys.stdin.readline())

deque = []

for i in range(a):
    n = sys.stdin.readline().split()
    command = n[0]
    if command == 'push_front':
        num = n[1]
        deque.insert(0, num)
    if command == 'push_back':
        num = n[1]
        deque.append(num)
    if command == 'pop_front':
        if deque:
            popNum = deque.pop(0)
            print(popNum)
        else: 
            print(-1)
    if command == 'pop_back':
        if deque:
            popNum = deque.pop()
            print(popNum)
        else: 
            print(-1)
    if command == 'size':
        size = len(deque)
        print(size)
    if command == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    if command == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    if command == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
    

