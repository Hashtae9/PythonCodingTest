import sys
a, b, c = map(int,sys.stdin.readline().split())
print(f'{(a+b)%c}')
print(f'{((a%c) + (b%c))%c}')
print(f'{(a*b)%c}')
print(f'{((a%c) * (b%c))%c}')