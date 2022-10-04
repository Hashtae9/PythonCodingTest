import sys
a = int(sys.stdin.readline())

queue = []

for i in range(a):
    n = sys.stdin.readline().split()
    command = n[0]
    if command == 'push':
        num = n[1]
        queue.append(num)
    if command == 'pop':
        if queue:
            popNum = queue.pop(0)
            print(popNum)
        else: 
            print(-1)
    if command == 'size':
        size = len(queue)
        print(size)
    if command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    if command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    if command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    

