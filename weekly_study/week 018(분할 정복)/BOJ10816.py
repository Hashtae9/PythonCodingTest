# 숫자 카드 2
import sys

input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))

dic = dict()

count = 0
register = card[0]

for i in card:
    if i != register:
        dic[register] = count
        count = 1
        register = i

    else :
        count+=1
dic[register] = count

def binary_check(arr, target, start, end):
    while start <= end:
        mid = (start + end) //2

        if arr[mid] == target: return mid
        elif arr[mid] > target: end = mid-1
        else: start = mid+1
    return None

a = list(dic.keys())

for i in check:
    if binary_check(a, i, 0, len(a)-1) is not None:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')