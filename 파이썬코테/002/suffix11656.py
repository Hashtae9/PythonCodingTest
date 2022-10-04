import sys
n = list(sys.stdin.readline().rstrip())

temp = ''
result = []


while n:
    temp = n.pop() + temp
    result.append(temp)

result.sort()
for i in result:
    print(i)