import sys
a = int(sys.stdin.readline())

for i in range(a):
    word = sys.stdin.readline().split()
    for i in word:
        for j in range(len(i)):
            print(i[-j-1], end='') 
        print(' ', end='')
    # for j in word:
    #     print(j[::-1], end=' ')
    # print('')