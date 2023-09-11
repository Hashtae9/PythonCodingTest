import sys

INF = sys.maxsize
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dist = [[INF]*(n+1) for j in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # 버스가 a에서 b로 가는게 1개가 아닐 수 있음, 가장 가격이 작은걸 저장해야함
    dist[a][b] = min(c, dist[a][b])

def floyd_Warshall(d):

    for k in range(1, n+1): # 거치는 점
        for i in range(1, n+1): # i, j 체크
            for j in range(1, n+1):
                if d[i][j] > d[i][k] + d[k][j]: # 최솟값으로 변경
                    d[i][j] = d[i][k] + d[k][j]

                # 못가는 부분은 0으로 표시
                if i == j:
                    d[i][j] =0

    return d

result = floyd_Warshall(dist)

for i in range(1, n+1):
    for j in range(1, n+1):
        if result[i][j] == INF:
            result[i][j]=0

for line in result[1:n+1]:
    print(*line[1:n+1])