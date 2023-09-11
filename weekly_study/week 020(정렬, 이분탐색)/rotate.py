def rotate_90(list_2d):
    n = len(list_2d)
    m = len(list_2d[0])
    new = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    return new

def rotate_180(list_2d):
    n = len(list_2d)
    m = len(list_2d[0])
    new = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new[m-j-1][n-i-1] = list_2d[i][j]
    return new
#mj1 ni1
def rotate_270(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][i] = list_2d[i][j]
    return new


map = [[i for i in range(4)] for j in range(5)]
print(map)
def select_change(x, y, board):
    new = []
    for i in range(x, x+3):
        new.append(board[i][y:y+3])

print(len(map))
print(len(map[0]))

result = rotate_90(select_change(2, 1, map))

print(result)

def change_value(x, y, board, changed):
    for i in range(x, x+3):
        for j in range(y, y+3):
            board[i][j] = changed[i-x][j-y]

change_value(2, 1, map, result)
print(map)


test = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(rotate_90(test))

for i in range(1,12):
    if i == 7:
        print(7)
    else:
        print("7아님")