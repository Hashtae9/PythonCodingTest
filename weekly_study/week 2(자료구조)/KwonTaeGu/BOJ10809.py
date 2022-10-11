#알파벳 찾기
import sys

text = list(sys.stdin.readline().rstrip())

loc = [-1]*26

for i in range(len(text)):
    a = ord(text[i])-ord('a')
    if loc[a] == -1:
        loc[a] = i

print(" ".join(list(map(str, loc))))