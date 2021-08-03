# https://www.acmicpc.net/problem/1463
import sys
f = sys.stdin.readline

n = int(f())

dp = [0] * 10

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])
