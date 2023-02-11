#N-Queen
# https://sso-feeling.tistory.com/415
n = int(input())
ans = 0
row = [0] * n #인덱스는 행, 값은 열

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n): # 각 행에 퀸 놓기
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)

'''
n = int(input())
visited = [[0]*n for _ in range(n)]
log_x = []
log_y = []
result = 0
def dfs(x, y, cnt):
    global result
    if cnt == n: result +=1; return

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:#방문한적 없는곳
                if i not in log_x and j not in log_y:
                    log_x.append(i)
                    log_y.append(j)
                    visited[i][j] = 1
                    dfs(i, j, cnt+1)
                    log_x.pop()
                    log_y.pop()
                    visited[i][j] = 0

for i in range(n):
    for j in range(n):
        visited[i][j] = 1
        log_x.append(i)
        log_y.append(j)
        dfs(i, j, 1)
        log_x.pop()
        log_y.pop()

print(result)
'''