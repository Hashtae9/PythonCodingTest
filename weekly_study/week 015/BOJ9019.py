# DSLR
import sys
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    visited = ['']*10000 # 0부터 9999까지
    start, end = map(int, sys.stdin.readline().strip().split())
    
    def dfs():
        q = deque()
        q.append(start)
        visited[start] = 'k'
        
        while q:
            a = q.popleft()
            #d연산
            result_d = (a*2)%10000
            if visited[result_d] == '':
                visited[result_d] = visited[a]+'D'
                q.append(result_d)
            if result_d == end: return visited[a][1:]+'D'
            #s연산
            result_s = 9999
            if a != 0: result_s = a-1
            if visited[result_s] == '':
                visited[result_s] = visited[a]+'S'
                q.append(result_s)
            if result_s == end: return visited[a][1:]+'S'
            #L연산
            s_a1 = str(a)
            if len(s_a1) !=4:
                count = 4 - len(s_a1)
                for i in range(count):
                    s_a1 = '0'+s_a1
            result_l = int(s_a1[1]+s_a1[2]+s_a1[3]+s_a1[0])
            if visited[result_l] == '':
                visited[result_l] = visited[a]+'L'
                q.append(result_l)
            if result_l == end: return visited[a][1:]+'L'
            #R연산
            s_a2 = str(a)
            if len(s_a2) !=4:
                count = 4 - len(s_a2)
                for i in range(count):
                    s_a2 = '0'+s_a2
            result_r = int(s_a2[3]+s_a2[0]+s_a2[1]+s_a2[2])
            if visited[result_r] == '':
                visited[result_r] = visited[a]+'R'
                q.append(result_r)
            if result_r == end: return visited[a][1:]+'R'

    print(dfs())