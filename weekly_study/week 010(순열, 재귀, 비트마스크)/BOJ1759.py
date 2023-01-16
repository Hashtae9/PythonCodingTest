# 암호만들기
l, c = map(int, input().split())
alp = sorted(list(input().split()))
check = ['a', 'e', 'i', 'o', 'u']
s=[]
def dfs(start):
    if len(s) == l:
        a = 0 #자음
        b = 0 #모음
        for i in s:
            if i in check: b+=1
            else: a+=1
        if a>=2 and b>=1:
            print(''.join(s))
        return

    for i in range(start, c):
        if alp[i] not in s:
            s.append(alp[i])
            dfs(i+1)
            s.pop()
dfs(0)