# https://www.acmicpc.net/problem/2166
import sys
input = sys.stdin.readline

n = int(input())
xylist = [tuple(map(int, input().split())) for _ in range(n)]

first = 0
for i in range(1, n):
    first += xylist[i-1][0]*xylist[i][1] - xylist[i-1][1]*xylist[i][0]
first += xylist[n-1][0]*xylist[0][1] - xylist[n-1][1]*xylist[0][0]
first /= 2
first = abs(first)

print(float(first))
