def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2

    return answer

''' 시간초과
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

n = 5
distance = 0
cap = 4
sum_del = sum(deliveries)
sum_pic = sum(pickups)

while not ((sum_del == 0) and (sum_pic == 0)):
    count = cap
    long_del = 0
    long_pic = 0
    # del먼저 구하기
    for i in range(n-1, -1, -1):
        if deliveries[i] == 0:
            continue
        else:
            long_del = max(i+1, long_del)
            if deliveries[i] <= count:
                count -= deliveries[i]
                sum_del -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= count
                sum_del -= count
                count = 0
                break
    count = cap
    #pic구하기
    for j in range(n-1, -1, -1):
        if pickups[j] == 0:
            continue
        else:
            long_pic = max(j+1, long_pic)
            if pickups[j] <= count:
                count -= pickups[j]
                sum_pic -= pickups[j]
                pickups[j] = 0
            else:
                pickups[j] -= count
                sum_pic -= count
                count = 0
                break
    distance += 2*max(long_del, long_pic)

print(distance)
'''