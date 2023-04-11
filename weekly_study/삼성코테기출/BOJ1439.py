#뒤집기
s = input()
zero = 0
for i in s.split('1'):
    if i != '': zero+=1
one = 0
for j in s.split('0'):
    if j != '': one+=1
print(min(zero, one))