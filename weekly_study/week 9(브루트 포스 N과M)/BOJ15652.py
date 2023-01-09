#n과 m 4
n,m = map(int, input().split())

s=[]
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if s:
            if i >= s[-1]:
                s.append(i)
                dfs()
                s.pop()
        else:
            s.append(i)
            dfs()
            s.pop()
dfs()

'''
n,m = map(int, input().split())
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)
'''