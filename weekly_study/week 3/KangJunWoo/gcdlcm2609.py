import sys
a, b = map(int,sys.stdin.readline().split())

gcd = 0
lcm = a*b

while b != 0:
    a, b = b, a%b

gcd = a
lcm = lcm/gcd
print(gcd)
print(int(lcm))

# 최대공약수 구하기 유클리드 호제법
# a,b에 대하여 a/b의 나머지와 b의 공약수가 최대공약수
# 하나가 0이 될때까지 하면 나머지가 최대공약수
# 
