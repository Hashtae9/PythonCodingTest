import sys

initialString = sys.stdin.readline().strip()
initialString = list(initialString)
initialString.append(':')

a = int(sys.stdin.readline())

for i in range(a):
    index = initialString.index(':')
    commands = sys.stdin.readline().split()
    if commands[0] == 'L':
        if index != 0:
            initialString[index], initialString[index-1] = initialString[index-1], initialString[index]
    if commands[0] == 'D':
        if index != len(initialString)-1:
            initialString[index], initialString[index+1] = initialString[index+1], initialString[index]
    if commands[0] == 'B':
        if index != 0:
            del initialString[index-1]
    if commands[0] == 'P':
        initialString.insert(index, commands[1])

initialString.remove(':')
for i in initialString:
    print(i, end='')