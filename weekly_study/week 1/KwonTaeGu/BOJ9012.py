#괄호(9012번)
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    stk = []
    s = sys.stdin.readline()
    isVPS = True

    for ch in s:
        if ch == '(':
            stk.append('(')
        if ch == ')':
            if stk:
                stk.pop()
            #파이썬은 리스트가 비었는지 안비었는지 확인할때 not 리스트 의 꼴로 조건문을 만들 수 있음
            elif not stk:
                isVPS = False
                break
    if not stk and isVPS:
        print('YES')
    elif stk or not isVPS:
        print('NO')

