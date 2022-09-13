#요세푸스 문제(1158번)
N, K = map(int,input().split())
ans= []
arr = [i for i in range(1,N+1)]
num = 0

for i in range(N):
    num+=(K-1)
    if num >= len(arr):
        num %= len(arr)
    ans.append(str(arr.pop(num)))

print("<",', '.join(ans),">", sep="")

#print에 변수나 값을 쉼표로 구분해서 넣으면 출력될 때 공백이 생긴다. 따라서 sep="" 를 추가해줘야 <,> 와 숫자 사이에 공백이 생기지 않는다.