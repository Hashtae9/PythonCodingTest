#문자열 출력
import sys

while True:
    line = sys.stdin.readline().rstrip('\n')

    if not line:
        break
    a = list(line)
    result = [0]*4
    for i in a:
        if i.islower():
            result[0]+=1
        elif i.isupper():
            result[1]+=1
        elif i.isdigit():
            result[2]+=1
        elif i == ' ':
            result[3]+=1
    print("{} {} {} {}".format(result[0], result[1], result[2], result[3]))