import sys

text = list(sys.stdin.readline().rstrip())

alpha = [0]*26

for i in text:
    alpha[ord(i)-ord('a')] += 1

print(" ".join(list(map(str, alpha))))