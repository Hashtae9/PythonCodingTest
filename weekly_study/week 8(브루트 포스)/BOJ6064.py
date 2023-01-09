# 카잉 달력
import sys

def calculate(m, n, x, y):
    k = x #k를 x로 초기화
    while k <= m * n: #k의 범위는 m*n을 넘을 수 없기에
        if (k - x) % m == 0 and (k - y) % n == 0: #2개의 조건을 만족하는 k값을 찾는다.
            return k
        k += m #k-x가 m의 배수이기 때문에 k는 x로 초기화해주었기 때문에 m만 더해준다.
    return -1


t = int(input())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    print(calculate(m, n, x, y))


'''
처음에는 이해가 잘 안됬었는데, 생각해보면 x에다 M을 더하면 똑같이 x다. 
사실상 x는 고정해두고 y가 조건에 맞는지만 확인하면 된다는 것이다. 
x를 N으로 나눈 나머지가 y를 N으로 나눈 나머지와 같을 때까지 x에 M을 계속 더해주면 된다.

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    a, b, year = 0, 0, 0
    for _ in range(40001):
        if(a==x and b==y): print(year); break
        if(a == m): a -= m
        if(b == n): b -= n

        a+=1; b+=1; year+=1
        if(year == 40001): print(-1)
'''