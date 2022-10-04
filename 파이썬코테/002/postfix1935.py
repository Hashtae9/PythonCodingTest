import sys
from string import ascii_uppercase

n = int(sys.stdin.readline())

expression = list(sys.stdin.readline().strip())

alphabet_dict = {}

for i in range(n):
    alphabet_dict[ascii_uppercase[i]] = int(sys.stdin.readline()) 

stack = []

for i in expression:
    if i.isalpha():
        stack.append(alphabet_dict[i])
    else:
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i == '/':
            stack.append(a/b)

print(f"{stack[0]:.2f}")
print(round(stack[0], 3))
print(format(stack[0], ".2f"))
print("{:.2f}".format(stack[0]))
print(format(stack[0], ".2f"))

#https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1935-%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EC%8B%9D2-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python