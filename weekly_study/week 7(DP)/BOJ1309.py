# 동물원
n = int(input())
dp = [[0]*3 for i in range(100001)] # 빈칸 왼쪽 오른쪽
dp[0] = [0, 0, 0]
dp[1] = [1, 1, 1]

for i in range(2, n + 1):
    #전칸이 빈칸이면 이번에는 다 가능
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2])% 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2])% 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1])% 9901

print(sum(dp[n]) % 9901)