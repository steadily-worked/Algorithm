# 이것이 취업을 위한 코딩 테스트다 with 파이썬 동적계획법 실전문제
import sys
f = sys.stdin.readline

n, m = map(int, f().split())
a = [int(f()) for _ in range(n)]

dp = [10001] * (m+1)
# 일단, a에 있는 값들은 전부 dp[i]가 1이돼야함

dp[0] = 0
for i in range(n):
    for j in range(a[i], m+1):
        if dp[j-a[i]] != 10001:
            dp[j] = min(dp[j], dp[j-a[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
