# 트리의 높이와 너비
import sys
input = sys.stdin.readline
def inorder(root, level):
    global num
    if s[root][0] != -1:
        inorder(s[root][0], level + 1)
    row[level].append(num)
    num += 1
    if s[root][1] != -1:
        inorder(s[root][1], level + 1)

n = int(input())
s = [[0] * 2 for i in range(n + 1)]
node = [0 for i in range(n + 1)]
row = [[] for i in range(n + 1)]
num = 1
for i in range(n):
    ro, le, ri = map(int, input().split())
    s[ro][0] = le
    s[ro][1] = ri
    node[ro] += 1
    if le != -1:
        node[le] += 1
    if ri != -1:
        node[ri] += 1
for i in range(1, n + 1):
    if node[i] == 1:
        root = i
inorder(root, 1)
result = max(row[1]) - min(row[1]) + 1
level = 1
for i in range(2, n + 1):
    if row[i]:
        if result < max(row[i]) - min(row[i]) + 1:
            result = max(row[i]) - min(row[i]) + 1
            level = i
print(level, result)

'''
import sys

n = int(sys.stdin.readline())
tree = {}
level = [0]*(n+1)
width = [0]*(n+1)
log_k = set()
log_v = set()
for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    log_k.add(root)
    log_v.add(left)
    log_v.add(right)
    tree[root] = [left, right]

find = (log_k - log_v).pop()

# 깊이는 preorder(중앙 -> 왼쪽노드 -> 오른쪽 노드
def preorder(root, depth):
    if root != '-1':
        level[int(root)] = depth
        preorder(tree[root][0], depth+1)
        preorder(tree[root][1], depth+1)

# 너비는 inorder(왼쪽 -> 중앙 -> 오른쪽)
w = 1
def inorder(root):
    global w
    if root != '-1':
        inorder(tree[root][0])
        width[int(root)] = w # 왼쪽으로 쭉 다 파고들었다면 너비에 1 추가
        w += 1
        inorder(tree[root][1])

preorder(str(find), 1)
inorder(str(find))

r1 = 0 #깊이
r2 = 0 #너비
for i in range(1, max(level)+1):
    if level.count(i) == 1:
        if r2 < 1:
            r1 = i; r2 = 1
    elif level.count(i) >=2:
        pos = [j for j in range(len(level)) if level[j] == i]
        if (width[pos[-1]] - width[pos[0]])+1 > r2:
            r1 = i; r2 = (width[pos[-1]] - width[pos[0]])+1

print(r1, r2)
'''