#연산자 끼워넣기
import itertools
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().strip().split()))
count = list(map(int, sys.stdin.readline().strip().split()))
buho = []
for i in range(4):
    if i == 0:
        for _ in range(count[i]):
            buho.append('+')
    elif i == 1:
        for _ in range(count[i]):
            buho.append('-')
    elif i == 2:
        for _ in range(count[i]):
            buho.append('*')
    elif i == 3:
        for _ in range(count[i]):
            buho.append('/')
per = list(itertools.permutations(buho, len(buho)))
result = []
for i in per: #부호마다 결과값이 다름
    a = num[0]
    for j in range(n-1):
        if i[j] == '+':
            a += num[j+1]
        elif i[j] == '-':
            a -= num[j+1]
        elif i[j] == '*':
            a *= num[j+1]
        elif i[j] == '/':
            a = int(a/num[j+1])
    result.append(a)
print(max(result))
print(min(result))

'''
# 백트래킹 (Python3 통과, PyPy3도 통과)
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
'''