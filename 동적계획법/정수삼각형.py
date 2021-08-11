# https://www.acmicpc.net/problem/1932
import sys
f = sys.stdin.readline
n = int(f())
a = [[int(x) for x in f().split()] for _ in range(n)]

dp = [[0] * i for i in range(1, n+1)]
dp[0][0] = a[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + a[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + a[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + a[i][j], dp[i-1][j] + a[i][j])

print(max(dp[-1]))
