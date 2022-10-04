import sys
a = [True for i in range(1000000)]

for i in a:
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print(i)