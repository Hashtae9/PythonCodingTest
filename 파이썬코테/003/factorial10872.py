def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())    
a = list(str(factorial(n)))
a = a[::-1]
result = 0
for i in a:
    if i != '0':
        break
    else:
        result += 1
print(result)
