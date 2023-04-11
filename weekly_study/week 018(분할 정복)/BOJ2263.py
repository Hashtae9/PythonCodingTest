# 트리의 순회
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위 순회의 값들의 인덱스값을 저장
nodeNum = [0] * (n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i

# 분할 정복 방식으로 전위 순회를 찾음
def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return

    # 후위 순회 결과의 끝이 (서브)트리의 루트임을 이용
    root = postorder[postEnd]

    leftNode = nodeNum[root] - inStart
    rightNode = inEnd - nodeNum[root]

    print(root, end = " ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, n - 1, 0, n - 1)