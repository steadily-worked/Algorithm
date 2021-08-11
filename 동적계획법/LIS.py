# https://www.acmicpc.net/problem/11053
import sys
f = sys.stdin.readline

n = int(f())
a = [int(x) for x in f().split()]
dp = [1] * 1001

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
