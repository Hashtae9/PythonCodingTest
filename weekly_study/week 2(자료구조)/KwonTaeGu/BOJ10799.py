#쇠막대기(10799번)
import sys

text = list(sys.stdin.readline().rstrip())
memory = []
lazer = False
stick = 0

for i in range(len(text)):
    if text[i] == '(':
        memory.append('(')
    elif text[i] == ')':
        if text[i-1] == '(':
            memory.pop()
            stick += len(memory)
        else:
            memory.pop()
            stick += 1

print(stick)