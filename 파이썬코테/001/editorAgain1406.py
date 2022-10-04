import sys

leftString = list(sys.stdin.readline().strip())
rightString = []

a = int(sys.stdin.readline())

for i in range(a):
    commands = sys.stdin.readline().split()
    if commands[0] == 'L':
        if leftString:
            rightString.append(leftString.pop())

    if commands[0] == 'D':
        if rightString:
            leftString.append(rightString.pop())
        
    if commands[0] == 'B':
        if leftString:
            leftString.pop()

    if commands[0] == 'P':
        leftString.append(commands[1])

# print(''.join(leftString), end='')
# print(''.join(rightString[::-1]))

print(f'{"".join(leftString)}{"".join(rightString[::-1])}')
a = 101
print(a, 'dff')
print(f'{a}는 ㅇ랑러ㅓㄹ비')

print('dfff', end='', sep=)
print('abc')