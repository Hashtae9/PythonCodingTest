#에디터(1406번)
import sys

#문자열 받아오기
str = list(sys.stdin.readline().rstrip())
print(str)
list_r = []
list_l = []

for s in str:
    list_l.append(s)

#명령어 나올 횟수
n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().split()
    #P명령어 수행
    if s[0] == "P":
        list_l.append(s[1])

    #L명령어 수행
    if s[0] == "L" and list_l:
            list_r.append(list_l.pop())

    #D명령어 수행
    if s[0] == "D" and list_r:
            #list_r의 제일 앞 원소를 빼서 list_l의 제일 끝에 붙이기
            list_l.append(list_r.pop(0))

    #B명령어 수행
    if s[0] == "B" and list_l:
            list_l.pop()

list_total = list_l+list_r
print("".join(list_total))

#input() -> 받을때 엔터(/n)까지 받아오지 않음
#sys.stdin.readLine() -> 받을때 엔터까지 받아옴 ///따라서 .rstrip()으로 개행문자를 제거해줌