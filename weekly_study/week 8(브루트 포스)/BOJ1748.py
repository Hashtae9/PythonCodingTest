# 수 이어쓰기1
n = int(input())
a = 1
result = 0
length = len(str(n))

for i in range(length):
    if i+1 == length:
        result += a*((n - (10**i))+1)
    else:
        result += a*9*(10**i)
    a += 1
print(result)

# 1 ~ 9 = 9
# 10 ~ 99 = 90
# 100 ~ 999 = 900