# https://www.acmicpc.net/problem/14501
import sys
f = sys.stdin.readline

n = int(f())

t_list = []
p_list = []
for i in range(n):
    t, p = map(int, f().split())
    t_list.append(t)
    p_list.append(p)

dp = [0] * 16

for i in range(n):
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]
    if dp[i + t_list[i]] < dp[i] + p_list[i]:
        dp[i + t_list[i]] = dp[i] + p_list[i]

print(dp[n])
