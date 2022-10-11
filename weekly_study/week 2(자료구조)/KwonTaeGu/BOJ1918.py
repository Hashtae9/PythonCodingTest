#후위 표기식
strn =list(input())
stack=[]
res=''
for s in strn:
    if s.isalpha():
        res+=s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)


'''
import sys

text = list('A*(B+C)')#sys.stdin.readline().rstrip().split()

def level(i):
    if i == '(' or i == ')':
        return 2
    elif i == '*' or i == '/':
        return 1
    elif i == '+' or i == '-':
        return 0
    else : return -1

buho = []
result = []
send = []

storage = 0

for t in range(len(text)):
    if text[t]== '+' or text[t] == '-':
        if buho:
            if level(buho[-1]) == 1:
                buho.appned(text[t])
                send = buho
            elif level(buho[-1] == 2):
                buho.append(text[t])
        else:
            buho.appned(text[t])

    elif text[t] == '*' or text[t] == '/':
        if buho:
            if level(buho[-1])==2:
                buho.appned(text[t])
            elif level(buho[-2]) == 1:

        else:
            buho.appned(text[t])
    elif text[t] == '(' or text[t] == ')':
        if


print(result)
'''