# 나무 자르기
n, k = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in tree:
        count += (i - mid if i >= mid else 0)
    if count >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)