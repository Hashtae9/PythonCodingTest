# 코테 파이썬 정리집(그래프, 그래프 탐색(BFS, DFS))

## 그래프

<img src="https://user-images.githubusercontent.com/101400894/212793723-c251ba8e-32e5-455d-8872-ddd6507a9093.png" alt="image" style="zoom:47%;" ALIGN="LEFT"/>

> 파이썬에서는 그래프를 딕셔너리를 이용하여 나타냄

```
graph = {1 : [2,3,4], 2 : [5], 3 : [5], 4 : [], 5 : [6, 7], 6 : [], 7 : [3]}
```



### 그래프(딕셔너리를 이용한)

```python
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited) # - 연산자 사용가능 이점
    return visited
  
print(BFS_with_adj_list(graph_list, root_node))

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited) # - 연산자 사용가능 이점
    return visited

print(BFS_with_adj_list(graph_list, root_node))
```





## dfs

```python
def dfs(v):
    v를 이미 방문한 곳으로 처리한다 
    for 각각의 v에 연결된 모든 정점 i에 대해서:
        if i에 방문하지 않았다면:
            dfs(i)

def dfs(v,visited=[]):
    visited.append(v)
    for i in graph[v]:
        if not i in visited:
            visited = dfs(i,visited)
    return visited # [1,2,5,6,7,3,4]
```



## bfs

```python
def bfs(v):
    큐 선언 
    v를 이미 방문한 곳으로 처리 
    v를 큐에 추가해준다 
    while 큐가 비어있지 않다면:
        큐에서 v를 pop해준다 
        for v에 연결된 각각의 정점 i에 대하여:
            if i에 아직 방문하지 않았다면:
                i를 방문한 곳으로 처리한다 
                큐에 i를 추가한다

from collections import deque
que = deque()

def bfs(v): 
    visited = [v]
    que = [v]
    while que:
        v = que.popleft(0)
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                que.append(i)
    return visited # [1, 2, 3, 4, 5, 6, 7]
```

