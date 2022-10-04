import sys
a = int(sys.stdin.readline())

stackSequence = []
willPrinted = []
isSequence = True
stackNum = 1

for i in range(a):
    inputNum = int(sys.stdin.readline())
    while stackNum <= inputNum:
        stackSequence.append(stackNum)
        stackNum += 1
        willPrinted.append('+')
    if stackSequence[-1] == inputNum:
        stackSequence.pop()
        willPrinted.append('-')
    else:
        isSequence = False
        print("NO")
        break

if isSequence:
    for i in willPrinted:
        print(i)

        