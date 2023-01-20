# 단지 번호 붙이기
n = int(input())
house = [list(input()) for i in range(n)]
visited = [[False]*n for i in range(n)]

def check(i, j):
    global num
    if i == n or j == n or i == -1 or j == -1:
        return

    if visited[i][j] == False:
        visited[i][j] = True
        if house[i][j] == '1':
            num+=1
            check(i, j-1)
            check(i, j+1)
            check(i+1, j)
            check(i-1, j)
        return
    return

house_count = []
for i in range(n):
    for j in range(n):
        num = 0
        check(i, j)
        if num != 0:
            house_count.append(num)
print(len(house_count))
for i in sorted(house_count): print(i)