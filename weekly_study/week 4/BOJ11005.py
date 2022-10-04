#진법 변환 2
import sys

n, b = map(int, sys.stdin.readline().split())

array1 = [i for i in range(9+1)]
array2 = [chr(i) for i in range(65, 90+1)]
array_res = array1+array2

res = ''
while n!=0:
    res = str(array_res[n%b]) + res
    n = n//b
print(res)
