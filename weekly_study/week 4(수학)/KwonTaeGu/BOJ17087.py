#숨바꼭질6
import sys
import math

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
gcd_num = [abs(i-s) for i in num]

cal_gcd = gcd_num[0]

for i in gcd_num[1:]:
    cal_gcd = math.gcd(i, cal_gcd)

print(cal_gcd)