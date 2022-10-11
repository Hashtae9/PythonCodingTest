import sys
# a = int(sys.stdin.readline())
a = 8

stackSequence = []
stack = []
printed = []
willPrinted = []
able = True
# stack 저장을위한 num
stackNum = 0
# 수열을 위한 num
sequenceNum = 0

# for i in range(a):
#     # stackSequence.append(int(sys.stdin.readline().strip()))
stackSequence = [4, 3, 6, 8, 7, 5, 2, 1]

for j in range(stackSequence[sequenceNum]):
    stackNum += 1
    stack.append(stackNum)
    willPrinted.append('+')

printed.append((stack.pop()))
willPrinted.append('-')
sequenceNum += 1

while sequenceNum < len(stackSequence):
    if stackSequence[sequenceNum] in printed:
        print('NO')
        able = False
        break
    if stackSequence[sequenceNum] < stackNum:
        printed.append((stack.pop()))
        willPrinted.append('-')
        while printed[-1] != stackSequence[sequenceNum]:
            printed.append(stack.pop())
            willPrinted.append('-')
        sequenceNum += 1
    else:
        while stackNum != stackSequence[sequenceNum]:
            stackNum += 1 
            stack.append(stackNum)
            willPrinted.append('+')
        printed.append((stack.pop()))
        willPrinted.append('-')
        sequenceNum += 1

print(willPrinted)
