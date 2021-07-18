# https://www.acmicpc.net/problem/11497
import sys
from collections import deque
f = sys.stdin.readline

t = int(f())
def a():
    n = int(f())
    l_list = list(map(int, f().split()))
    empty_list = deque()
    sorted_l = sorted(l_list, reverse=True)
    sorted_max = sorted_l[0]
    dif_list = []
    empty_list.append(sorted_max)
    for j in range(1, len(sorted_l)):
        if j % 2 == 0:
            empty_list.appendleft(sorted_l[j])
        else:
            empty_list.append(sorted_l[j])

    ans = 0
    for i in range(n):
        if i == n-1:
            j = 0
        else:
            j = i + 1
        ans = max(ans, abs(empty_list[i] - empty_list[j]))
    return ans

for i in range(t):
    print(a())