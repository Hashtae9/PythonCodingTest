# 돌 그룹
import collections


def bfs(a, b, c):
    q = collections.deque()
    q.append([a, b, c])
    V[a][b] = 1
    while q:
        a, b, c = q.popleft()
        if a == b and b == c and c == a:
            return 1
        if a > b and not V[a - b][2 * b]:
            V[a - b][2 * b] = 1
            q.append((a - b, 2 * b, c))
        if a < b and not V[2 * a][b - a]:
            V[2 * a][b - a] = 1
            q.append((2 * a, b - a, c))
        if b > c and not V[b - c][2 * c]:
            V[b - c][2 * c] = 1
            q.append((a, b - c, 2 * c))
        if b < c and not V[2 * b][c - b]:
            V[2 * b][c - b] = 1
            q.append((a, 2 * b, c - b))
        if c > a and not V[2 * a][c - a]:
            V[2 * a][c - a] = 1
            q.append((2 * a, b, c - a))
        if c < a and not V[a - c][2 * c]:
            V[a - c][2 * c] = 1
            q.append((a - c, b, 2 * c))
    return 0

A, B, C = map(int, input().split())
V = [[0] * 1500 for _ in range(1500)]
print(bfs(A, B, C))