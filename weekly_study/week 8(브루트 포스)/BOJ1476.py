# 날짜 계산
a, b, c = map(int, input().split())

e, s, m, year = 1, 1, 1, 1

while True:
    if a==e and b==s and c==m:
        break
    e += 1
    s += 1
    m += 1
    year += 1
    if e == 16: e = 1
    if s == 29: s = 1
    if m == 20: m = 1
print(year)