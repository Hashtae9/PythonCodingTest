#단어 뒤집기2(17413)
import sys

ans = []
memory = []
specific = False

text = list(sys.stdin.readline().rstrip())

for i in text:
    if specific:
        if i == '>':
            specific = False
            memory.append(i)
            ans.append("".join(memory))
            memory.clear()
        else:
            memory.append(i)
    else:
        if i == '<':
            specific = True
            ans.append("".join(memory)[::-1])
            memory.clear()
            memory.append(i)
        elif i == ' ':
            ans.append("".join(memory)[::-1])
            memory.clear()
            ans.append(i)
        else:
            memory.append(i)

ans.append("".join(memory)[::-1])
print("".join(ans))