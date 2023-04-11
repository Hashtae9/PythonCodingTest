# 로봇청소기
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
r, c, d = map(int, input().split()) #d 북 동 남 서

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

board = [list(map(int, input().split())) for _ in range(N)]
clean_count = 0
def cleaner(x, y, direction):
    global clean_count

    # 현재있는칸이 청소가 x
    if board[x][y] == 0:
        clean_count +=1
        board[x][y] = 2 #청소된 곳 표시
        cleaner(x, y, direction)
        return

    isBlank = blank_check(x, y)

    if isBlank: #빈칸이 있다면
        direction = direction-1 if direction!=0 else 3
        nx = x+dx[direction]
        ny = y+dy[direction]
        if board[nx][ny] == 0: cleaner(nx, ny, direction) #청소안된 곳으로 이동
        else: cleaner(x, y, direction)# 방향만 바뀜
    else: #빈칸이 없다면
        nx = x+(dx[direction]*(-1))
        ny = y+(dy[direction]*(-1)) #역방향
        if 0<=nx<N and 0<=ny<M and board[nx][ny] != 1: #이동가능하다면
            cleaner(nx, ny, direction)
    return

# 4방향에 청소안된곳 확인
def blank_check(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 0:
                return True
    return False #빈칸 없음

cleaner(r, c, d)
print(clean_count)