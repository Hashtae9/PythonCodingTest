#최대공약수와 최소 공배수
import math
a, b = map(int, input().split())

print(math.gcd(a,b))
print(math.lcm(a,b))

'''
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b //gcd(a,b)
    
'''