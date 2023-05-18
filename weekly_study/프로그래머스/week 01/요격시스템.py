def solution(result):
    print(result)
    return result

tar = (input().replace('[', '').replace(']', '')).split(',')
target = []
for i in range(0, len(tar), 2):
    a, b = tar[i], tar[i+1]
    a = int(a.strip())
    b = int(b.strip())
    target.append([a, b])

target.sort(key = lambda x: (x[0], x[1]))

cover = -1
result = 0
for s, e in target:
    if s >= cover: # 미사일이 커버범위 밖
        result+=1
        cover = e
solution(result)