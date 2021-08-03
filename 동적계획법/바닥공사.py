# 이것이 취업을 위한 코딩 테스트다 with 파이썬 동적계획법 실전문제
n = int(input())

# 2*1 = 1가지
# 2*2 = 3가지 (각 1번씩)
# 2*3 = 5가지 (2*2 3가지에 + 2 * 1 두번 더하기)
# 2*4 = 11가지 (2*3 5가지에 2 * 2 두번 더하기)
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2]) % 796796

print(dp[n])
