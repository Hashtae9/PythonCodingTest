#팩토리얼 0의 개수
def count_two(n):
    a = n
    count = 0
    while True:
        if a%2 == 0:
            a = a/2
            count+=1
        else:
            return count

def count_five(n):
    a = n
    count = 0
    while True:
        if a%5 == 0:
            a = a/5
            count+=1
        else:
            return count

def count_zero(n):
    if n==0 or n==1:
        return 0

    count_t = 0
    count_f = 0
    for i in range(2, n+1):
        count_t += count_two(i)
        count_f += count_five(i)

    return min(count_t, count_f)

print(count_zero(int(input())))