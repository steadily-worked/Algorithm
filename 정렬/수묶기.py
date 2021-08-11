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

# 합이 최대가 되려면..
# -10 -5 -3 -1 1 3 5 7 10
# 10*7 + 5*3 + 1 + (-1*-3) + (-5*-10)
# 일단, 양수는 1개 남을때까지 전부 2개씩 묶어서 곱해주고, 마지막 하나는 더해준다.
# 그다음에, sort()한다음, 전체 음수가 홀수개라면 역시 1개 남을때까지 전부 2개씩 묶어서 곱해주고, 마지막 하나는 더해준다.
# 전체 음수가 짝수개라면 전부 묶어서 곱해준다.

# 5 / 10 7 5 3 1 합이 최대가 되려면..
# -10 -5 -3 -1 1 3 5 7 10
# 10*7 + 5*3 + 1 + (-1*-3) + (-5*-10)
# 일단, 양수는 1개 남을때까지 전부 2개씩 묶어서 곱해주고, 마지막 하나는 더해준다.
# 그다음에, sort()한다음, 전체 음수가 홀수개라면 역시 1개 남을때까지 전부 2개씩 묶어서 곱해주고, 마지막 하나는 더해준다.
# 전체 음수가 짝수개라면 전부 묶어서 곱해준다.
# 근데, 두개 남았는데 남은 두개 중 하나라도 1이라면, 곱해주는거보단 그냥 더해주는 게 결과값이 더 크다. (양수 기준)
# 음수라면..? 그냥 앞에서 계속 곱해주고 pop해서 빼준 다음에, -1만 남았으면 더해주고 -1과 0이 같이 남았으면 곱해주고


# 5 / 10 7 5 3 1
