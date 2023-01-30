# 트리 순회
import sys
n = int(sys.stdin.readline().strip())
tree = {} #딕셔너리 사용 key, value형태 이용

#트리에 값 집어 넣기
for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0]) # left 왼쪽먼저 쭉 출력
        preorder(tree[root][1]) # right 왼쪽 후 오른쪽 출력

def inorder(root):
    if root != '.':
        inorder(tree[root][0]) #왼쪽먼저 쭉 들어가서 root 출력
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root !='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')