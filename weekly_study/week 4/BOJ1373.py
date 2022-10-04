#2진수 8진수
print(oct(int(input(), 2))[2:])

'''
n = input()

if len(n)%3 == 1:
    n = '00'+ n
elif len(n)%3 == 2:
    n = '0'+ n

result = ''
for i in range(0, len(n), 3):
    s = n[i:i+3]
    count = 0
    if s[0] == '1':
        count+=4
    if s[1] == '1':
        count+=2
    if s[2] == '1':
        count+=1
    result = result+str(count)
print(result)
'''