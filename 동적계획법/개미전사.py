# 이것이 취업을 위한 코딩 테스트다 with 파이썬 동적계획법 실전문제
import sys
f = sys.stdin.readline

n = int(f())
a = list(map(int, f().split()))

dp = [0] * 100

dp[0] = a[0]
dp[1] = max(a[0], a[1])

for i in range(2, n):
    dp[i] = max(dp[i-2] + a[i], dp[i-1])

print(dp[n-1])
