#조합의 0의 개수
import sys
n, m = map(int, sys.stdin.readline().split())

def count_number(n, k):
    count = 0
    while n:
        n //=k
        count+= n
    return count

five_count = count_number(n,5)-count_number(m,5)-count_number(n-m,5)
two_count = count_number(n,2)-count_number(m,2)-count_number(n-m,2)
print(min(two_count, five_count))

'''
https://tmdrl5779.tistory.com/95

def count_two(num):
    count = 0
    for i in range(1, num+1):
        a=i
        b=True
        while b:
            if a%2==0:
                a=a/2
                count+=1
            if a%2!=0:
                b=False
    return count

def count_five(num):
    count = 0
    for i in range(1, num+1):
        a=i
        b=True
        while b:
            if a%5==0:
                a=a/2
                count+=1
            if a%5!=0:
                b=False
    return count

upper_t = count_two(n)
upper_f = count_five(n)
lower_t = count_two(m)+count_two(l)
lower_f = count_five(m)+count_five(l)

print(min(upper_t-lower_t, upper_f-lower_f))

'''