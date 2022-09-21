import sys

text = sys.stdin.readline()

result = ''
for t in text:
    if t == ' ':
        result+=' '
    elif t.islower():
        if (ord(t)+13) > ord('z'):
            result += chr(ord('a')+ ord(t)+13 - ord('z') -1)
        else: result += chr(ord(t)+13)
    elif t.isdigit():
        result += t
    elif t.isupper():
        if (ord(t)+13) > ord('Z'):
            result += chr(ord('A')+ ord(t)+13 - ord('Z') -1)
        else: result += chr(ord(t)+13)

print(result)

'''
s = input()
res = ''
for c in s:
    if 'a' <= c <= 'z':
        res += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
    elif 'A' <= c <= 'Z':
        res += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
    else:
        res += c
print(res)
'''