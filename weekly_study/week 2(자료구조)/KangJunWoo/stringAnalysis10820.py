import sys
from string import ascii_lowercase, ascii_uppercase

#try catch문으로 eof error 잡기

while True:
    n = sys.stdin.readline()
    if not n:
        break
    strn = []
    for i in n:
        strn.append(i)
    num_lower = 0
    num_upper = 0
    num_digit = 0
    num_space = 0
    for i in strn:
        if i in ascii_lowercase:
            num_lower += 1
        elif i in ascii_uppercase:
            num_upper += 1
        elif i.isdigit():
            num_digit += 1
        elif i == ' ':
            num_space += 1
    print(num_lower, num_upper, num_digit, num_space)
