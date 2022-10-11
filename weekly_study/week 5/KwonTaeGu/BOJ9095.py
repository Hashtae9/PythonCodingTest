#1, 2, 3 더하기
'''
1 1 //1
2 1+1, 2 //2
3 1+1+1, 1+2, 2+1, 3 //4
4 1111, 211(3), 22, 31(2)  //7
5 11111, 2111(4), 221(3), 311(3), 32(2) //13
6 111111, 21111(5), 2211(6), 222, 3111(4), 321(6), 33 //24
'''
import sys
n = int(sys.stdin.readline())
num = [0]*n

for i in range(n):
    num[i] = int(sys.stdin.readline())

dp = [0]*11
dp[0]=dp[1]=1
dp[2]=2
for i in range(3, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in num:
    print(dp[i])