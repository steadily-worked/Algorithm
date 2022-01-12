# https://www.acmicpc.net/problem/13702
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
start, end = 1, max(c)

while start <= end:
    temp = 0
    mid = (start + end) // 2
    for i in c:
        temp += (i // mid)
    if temp >= k:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)
