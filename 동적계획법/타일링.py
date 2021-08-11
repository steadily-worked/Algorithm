# https://www.acmicpc.net/problem/1793
import sys
f = sys.stdin.readline


def title(n):
    dp = [1] * 251
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
    return dp[n]


while True:
    try:
        print(title(int(f())))
    except:
        break
