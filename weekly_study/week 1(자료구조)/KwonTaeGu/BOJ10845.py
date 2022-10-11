#큐(10845번)
import sys

n = int(sys.stdin.readline().rstrip())

list = []

for _ in range(n):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == 'push':
        list.append(str[1])

    if str[0] == 'pop':
        if list:
            print(list.pop(0))
        else:
            print("-1")

    if str[0] == 'size':
        print(len(list))

    if str[0] == 'empty':
        if list:
            print("0")
        else:
            print("1")

    if str[0] == 'front':
        if list:
            print(list[0])
        else:
            print("-1")

    if str[0] == 'back':
        if list:
            print(list[-1])
        else:
            print("-1")