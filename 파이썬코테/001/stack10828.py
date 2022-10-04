import sys
a = int(sys.stdin.readline())

stack = []

for i in range(a):
    n = sys.stdin.readline().split()
    command = n[0]
    if command == 'push':
        num = n[1]
        stack.append(num)
    if command == 'pop':
        if stack:
            popNum = stack.pop()
            print(popNum)
        else: 
            print(-1)
    if command == 'size':
        size = len(stack)
        print(size)
    if command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    

