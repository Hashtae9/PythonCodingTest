# Guess
n = int(input())
arr = [[0] * n for _ in range(n)]
b = list(input())
v, k = [], 0


def possible(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += v[i]
        if arr[i][idx] == '+' and s <= 0:
            return False
        if arr[i][idx] == '0' and s != 0:
            return False
        if arr[i][idx] == '-' and s >= 0:
            return False
    return True

# dfs
def solve(idx):
    if idx == n:
        print(' '.join(map(str, v)))
        exit(0)
    for i in range(-10, 11):
        v.append(i)
        if possible(idx):
            solve(idx + 1)
        v.pop()


for i in range(n):
    for j in range(i, n):
        arr[i][j] = b[k]
        k += 1
solve(0)
