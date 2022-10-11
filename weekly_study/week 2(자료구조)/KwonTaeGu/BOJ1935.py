#후위표기식2
N=int(input())
expression=list(input())
num=[int(input()) for i in range(N)]

stk=[]

for i in expression:
    if i.isalpha():
        stk.append(num[ord(i)-65])
    else:
        a=stk.pop()
        result=stk.pop()

        if i=='+':
            result+=a

        elif i=='-':
            result-=a

        elif i=='*':
            result*=a

        elif i=='/':
            result/=a

        stk.append(result)

print('{:.2f}'.format(stk[-1]))
print(format(stk[-1], ".2f"))

'''
import sys

n = int(input())

text = list(sys.stdin.readline().rstrip())
num = [0]*n

for i in range(n):
    num[i] = input()

print(num)

buho = []
cal = []

compare = ['*', '/', '+', '-']
count = 1

for t in range(len(text)):
    if text[t] == '*' or text[t] == '/':
        buho.append(text[t])
        if t+1 == len(text) or text[t+1] != compare:
            for i in buho[::-1]:
                cal.insert(count, i)
                count+=2
            buho.clear()
    elif text[t] == '+' or text[t] == '-':
        buho.append(text[t])
        if t+1<len(text):
            if text[t+1] != compare:
                for i in buho[::-1]:
                    cal.insert(count, i)
                    count+=2
                buho.clear()

        elif t+1 == len(text):
            for i in buho[::-1]:
                cal.insert(count, i)
                count+=2
        print(cal)
    else:
        cal.append(text[t])
        print(cal)

total = []
for i in cal:
    temp = i.replace(i, num[ord(i) - ord('A')])
    total.append(temp)
print(temp)
'''