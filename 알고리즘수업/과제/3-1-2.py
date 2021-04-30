import sys


def stair(n, price):
    if 1 <= n <= 10000:  # n의 범위를 설정합니다.
        # price의 첫 번째 값에 0을 넣습니다. (혼란을 방지하기 위해서입니다. 0번째 계단에 오르는 방법은 0가지라고 가정했습니다.)
        price.insert(0, 0)
        # 0부터 n까지의 i 범위에 대해 전부 0을 넣은 dp 배열을 만들었습니다.
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1], dp[2], dp[3], dp[4] = price[0], price[1], price[1] + \
            price[2], price[3], price[4]
        # 1, 3, 4개씩 오를 수 있으므로 처음부터 4개의 계단까지는 오르는 방법을 직접 구합니다.
        # 다른 부분은 해당 계단의 비용이 그대로 들어가지만, dp[2]의 경우 한 번에 두 계단은 오를 수 없고 한 계단씩 두 번 올라가야 하므로 price[1] + price[2] 입니다.
        for i in range(5, n+1):  # 구할 수 있는 부분은 다 구하고, 그 뒷부분부터는 for문을 돌립니다.
            dp[i] = min(dp[i-1], dp[i-3], dp[i-4]) + price[i]
            # i번째 계단을 오르는데 드는 최소 비용은, (i-1번째 계단까지의 누적 비용, i-3번째 계단까지의 누적 비용, i-4번째 계단까지의 누적 비용)의 최소값에다가
            # 마지막 계단은 반드시 밟아야 하므로 price[i], 즉 i번째 계단의 비용을 더했습니다.
        return dp[n]  # 이제 for문이 끝났으므로, n번째 계단을 오르는데 드는 최소 비용 dp[n]을 반환합니다.


n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))
print(stair(n, price))
