import sys
a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

num_input = list(map(int, sys.stdin.readline().split()))

temp_decimal = 0
degree = 0

while num_input:
    temp_decimal += num_input.pop()*(a**degree)
    degree += 1

result = []
while temp_decimal != 0:
    result.append(temp_decimal%b)
    temp_decimal //= b

for i in result[::-1]:
    print(i, end=' ')