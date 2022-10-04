#base conversion
a, b = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))[::-1]

ten_num = 0
for i in range(m):
    ten_num += (a**i)*num[i]

res = []
while ten_num:
    res.append(str(ten_num%b))
    ten_num = ten_num//b
print(' '.join(res[::-1]))