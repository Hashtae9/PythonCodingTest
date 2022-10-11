#접미사 배열
import sys

text = sys.stdin.readline().rstrip()

dic = []

for i in range(len(text)):
    dic.append(text[i:])

dic.sort()

for i in dic:
    print(i)