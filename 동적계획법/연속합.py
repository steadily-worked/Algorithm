# https://www.acmicpc.net/problem/1912
n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = a[0]
if max(a) < 0:
    print(max(a))
else:
    for i in range(1, n):
        if dp[i-1] + a[i] > 0:
            dp[i] = dp[i-1] + a[i]

    print(max(dp))
