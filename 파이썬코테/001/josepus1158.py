import sys

a, b = map(int, sys.stdin.readline().split())

index = b-1

temp = []
willPrinted = []

for i in range(a):
    temp.append(i+1)

while temp:
    if index >= len(temp):
        index = index%len(temp)
    willPrinted.append(str(temp.pop(index)))
    index += (b-1)

print(f'<{", ".join(willPrinted)}>')

# print("<", ", ".join(willPrinted), ">", sep="")

