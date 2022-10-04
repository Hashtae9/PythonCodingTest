import sys
m, n = sys.stdin.readline().split()

n = int(n)
m = list(str(m))

result = 0
degree = 0

def convert(n):
    return ord(n)-55
for i in range(len(m)):
    if m[i].isalpha():
        m[i] = convert(m[i])

while m:
    result += int(m.pop())*(n**degree)
    degree += 1

print(int(result))