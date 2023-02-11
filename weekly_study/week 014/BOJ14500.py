#테트로미노
import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
'''
n, m = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for i in range(n)]
result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, depth):
    global result
    if depth == 4: result = max(result, cnt); return

    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m and visited[x+dx[i]][y+dy[i]] == False:
            if depth == 1: # ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
                visited[x+dx[i]][y+dy[i]] = True
                dfs(x, y, cnt+score[x+dx[i]][y+dy[i]], depth+1)
                visited[x+dx[i]][y+dy[i]] = False
            visited[x+dx[i]][y+dy[i]] = True
            dfs(x+dx[i], y+dy[i], cnt+score[x][y], depth+1)
            visited[x+dx[i]][y+dy[i]] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(n, m, 0, 0)
        visited[i][j] = False

print(result)'''