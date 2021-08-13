# https://www.acmicpc.net/problem/1744
import sys
f = sys.stdin.readline

n = int(f())
plus_list = []
minus_list = []
for i in range(n):
    a = int(f())
    if a > 0:
        plus_list.append(a)
    else:
        minus_list.append(a)

plus_list.sort()
minus_list.sort(reverse=True)

plus = 0
for i in range(len(plus_list)-1, -1, -2):
    if len(plus_list) % 2 == 0:
        if plus_list[i] != 1 and plus_list[i-1] != 1:
            plus += (plus_list[i] * plus_list[i-1])
        else:
            plus += plus_list[i] + plus_list[i-1]
    else:
        if len(plus_list) != 1:
            if plus_list[i] != 1 and plus_list[i-1] != 1:
                plus += (plus_list[i] * plus_list[i-1])
            else:
                plus += plus_list[i]
        else:
            plus += plus_list[i]

minus = 0
for i in range(len(minus_list)-1, -1, -2):
    if len(minus_list) % 2 == 0:
        minus += (minus_list[i] * minus_list[i-1])
    else:
        if len(minus_list) != 1:
            minus += (minus_list[i] * minus_list[i-1])
        else:
            minus += minus_list[i]
print(plus + minus)
