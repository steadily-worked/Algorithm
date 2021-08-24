# https://www.acmicpc.net/problem/9461
import sys
f = sys.stdin.readline

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
a = int(f())
for _ in range(a):
    n = int(f())
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[n])
