# 에너지 모으기
n = int(input())
wei = list(map(int, input().split()))

result = 0
def dfs(arr, energy):
    global result
    if len(arr) == 2: result = max(result, energy); return

    for j in range(1, len(arr)-1):
        b = arr[j-1]*arr[j+1]
        a = arr.pop(j) #해당 인덱스 지우기
        dfs(arr, energy+b)
        arr.insert(j, a) #해당 값 다시 넣어주기

dfs(wei, 0)
print(result)

