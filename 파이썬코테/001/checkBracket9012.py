import sys
a = int(sys.stdin.readline())

for i in range(a):
    stack = []
    isBracket = 'YES'
    bracket = sys.stdin.readline()
    bracket = list(bracket.strip())
    # 마지막이 '(' 이면 false
    if bracket[-1] == '(':
        isBracket = 'NO'
        print(isBracket)
        continue
    # '(' ')' 갯수가 다르면 false
    if bracket.count('(') != bracket.count(')'):
        isBracket = 'NO'
        print(isBracket)
        continue

    while bracket:
        # 마지막 요소가 ')'이면 스택에 저장
        if bracket[-1] == ')':
            stack.append(bracket.pop())
        # 마지막 요소가 '('이면 스택에 ')'가 있었는지 확인하고 있으면 계속, 없으면 false
        else:
            if stack:
                stack.pop()
                bracket.pop()
            else:
                isBracket = 'NO'
                break
    # 입력받은 문자열에 대해 반복문이 break없이 끝나면 true
    print(isBracket)