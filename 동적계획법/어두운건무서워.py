# https://www.acmicpc.net/problem/16507
import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(r)]

dp = [[0] * (c+1) for _ in range(r+1)]

for i in range(r+1):
    for j in range(c+1):
        dp[i][j] = pic[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for x in range(q):
    x1, y1, x2, y2 = list(map(int, input().split()))
    print((dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] +
           dp[x1-1][y1-1]) // ((x2-x1+1) * (y2-y1+1)))
