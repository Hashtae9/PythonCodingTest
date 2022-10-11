#스택 수열(1874번)
import sys

count = 1
#temp = True
stack = []
op = []

n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())

    while(count <= num):
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        print("NO")
        exit()
        #temp = False
        #break
'''
if(temp == False):
    print("NO")
else:
    for i in op:
        print(i)
'''
for i in op:
    print(i)

 