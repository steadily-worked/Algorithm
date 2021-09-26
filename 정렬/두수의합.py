# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
count = 0
first = 0
last = len(a)-1
a.sort()
while first < last:
    if a[first] + a[last] > x:
        last -= 1
    elif a[first] + a[last] < x:
        first += 1
    else:
        count += 1
        last -= 1
        first += 1
print(count)
