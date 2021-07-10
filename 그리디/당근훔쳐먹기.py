# https://www.acmicpc.net/problem/18234
import sys

f = sys.stdin.readline
n, t = map(int, f().split())

total_number = 0
w_list = []
for i in range(n):
    w_list.append(list(map(int, f().split())))
    total_number += w_list[i][0]

sorted_w_list = sorted(w_list, key=lambda x: (x[1]))

# 마지막 날부터, 영양제를 n-1번 준 것을 더해주고 pop한다.
for i in range(n-1, -1, -1):
    total_number += (sorted_w_list[-1][1] * (t-n+i))
    sorted_w_list.pop()

print(total_number)
