# 시험 감독
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0

for i in a:
    if i<b: count+=1;
    else:
        count +=1 # 총감독
        rest = i-b # 학생수 - 총감독이 감독한 학생 수
        count += rest//c if rest%c == 0 else (rest//c) +1
print(count)
