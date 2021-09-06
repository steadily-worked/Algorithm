# https://www.acmicpc.net/problem/14916
a = int(input())
count = 0

dp = [-1] * 100001
dp[2] = 1
dp[4] = 2
for i in range(5, a+1):
    z = i
    count = 0
    if i % 5 == 0:
        dp[i] = i // 5
    else:
        while z % 5 != 0:
            z -= 2
            count += 1
        count += (z // 5)
        dp[i] = count

print(dp[a])
