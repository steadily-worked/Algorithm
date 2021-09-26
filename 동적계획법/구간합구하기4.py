# https://www.acmicpc.net/problem/11659
import sys
f = sys.stdin.readline

n, m = map(int, f().split())
a = list(map(int, f().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + a[i-1]

for _ in range(m):
    first, last = list(map(int, f().split()))
    print(dp[last] - dp[first-1])
