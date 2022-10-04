# import sys
# stick = list(sys.stdin.readline().strip())
stick = ['(', ')', '(', '(', '(', '(', ')', '(', ')', ')', '(', '(', ')', ')', '(', ')', ')', ')', '(', '(', ')', ')']

temp = []
# ) 가 (다음 나오면 laser가 true
laser = True
stickNum = 0

# 입력 받은 문자열에 대하여 
for i in stick:
    # (이면 temp에 저장
    if i == '(':
        temp.append('(')
        laser = True
    else:
        if temp and laser:
            stickNum += (len(temp)-1)
        if temp and not laser:
            stickNum += 1
        temp.pop()

        laser = False


print(stickNum)