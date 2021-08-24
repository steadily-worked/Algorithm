# https://www.acmicpc.net/problem/9095
import sys
f = sys.stdin.readline
t = int(f())
for i in range(t):
    n = int(f())
    dp = [0] * 12

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])
