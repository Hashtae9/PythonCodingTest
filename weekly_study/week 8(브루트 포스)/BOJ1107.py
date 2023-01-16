# 리모컨

target = int(input())
n = int(input())
broken = list(map(int, input().split()))

pminus = abs(100-target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)


'''

n = int(input())
t = int(input())
broken = list(map(int, input().split()))

plusminus = abs(100-n)
channel = 0

def checknum(arr, number):
    for i in arr:
        if str(i) in str(number):
            return False
    return True

def channel(arr, num):
    for i in arr:
        if str(i) in str(num):
            up = num; down = num; count = 0
            while True:
                if checknum(arr, up):
                    return len(str(up)) + count
                if checknum(arr, up):
                    return len(str(down)) + count
                up += 1
                down -= 1
                count +=1

    return len(num)
print(min(channel(broken, n), plusminus))
'''