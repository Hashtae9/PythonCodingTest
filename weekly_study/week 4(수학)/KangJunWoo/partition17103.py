import sys

# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     else:
#         return True

m = int(sys.stdin.readline())



for i in range(m):
    n = int(sys.stdin.readline())
    result = 0
    for i in range((n//2)+1):
        temp_num = n - i
        if isPrime(i) and isPrime(temp_num):
            result += 1

    print(result)



