# 플로이드 워셜
import sys
INF = sys.maxsize

def floyd_Warshall(a):
    dist = [[INF]*n for i in range(n)] # 최단 경로를 담는 배열

    for i in range(n): # 최단 경로를 담는 배열 초기화
        for j in range(n):
            dist[i][j] = a[i][j]


    for k in range(n): # 거치는 점
        for i in range(n): # 시작점
            for j in range(n): # 28
                # k을 거쳤을 때의 경로가 더 작은 경로
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

n = 4 # 정점의 수

a = [[0, 5, INF, 8], [7, 0, 9, INF], [2, INF, 0, 4], [INF, INF, 3, 0]]
dist = floyd_Warshall(a)

for i in range(n):
    for j in range(n):
        print(dist[i][j] ,end=' ')
    print()