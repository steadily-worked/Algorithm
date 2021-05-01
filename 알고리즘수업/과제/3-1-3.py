import sys


def stair(n, k_num, price):
    if 1 <= n <= 10000:
        price.insert(0, 0)  # 혼란을 방지하기 위해 최초 인덱스 값에 0을 추가했습니다.
        # 0부터 n까지 0을 담은 DP배열 (i번째 계단까지 오르는 데 드는 비용의 최소를 나타내는 배열)을 만들었습니다.
        dp = [10000 for i in range(n + 1)]
        dp[0] = 0
        for i in range(n+1):  # k_num[0]부터 n번째까지의 계단에 대해서..
            for x in k_num:
                if i >= x:
                    dp[i] = min(dp[i], dp[i-x] + price[i])
                else:
                    break
        if dp[n] == 10000:
            return -1
        else:
            return dp[n]


n, k = map(int, sys.stdin.readline().split())
k_num = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
print(stair(n, k_num, price))
