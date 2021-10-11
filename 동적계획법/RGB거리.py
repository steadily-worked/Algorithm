# https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

n = int(input())
street = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = street[0]
for i in range(1, n):
    for j in range(len(street[i])):
        if j == 0:
            dp[i][j] = min(dp[i-1][-1], dp[i-1][1]) + street[i][j]
        elif j == len(street[i])-1:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][0]) + street[i][j]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]) + street[i][j]

print(min(dp[-1]))
