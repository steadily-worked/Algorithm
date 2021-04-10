n = int(input())

waitt = 0
arvt = []
judgt = []
total_time = 0
total_wait_time = 0
sum_arvt = []
sum_number = 0

for y in range(n):
    arvt_idx, judgt_idx = map(int, input().split())
    arvt.insert(y, arvt_idx)
    judgt.insert(y, judgt_idx)

sum_number = 0
sum_list = []
for i in arvt:
    sum_number += i
    sum_list.append(sum_number)

for i in range(0, n-1):  # n까지 돌면서
    total_time = sum_list[i] + waitt + judgt[i]
    if sum_list[i+1] >= total_time:
        waitt = 0
    else:
        waitt = total_time - sum_list[i+1]
    total_wait_time += waitt

print(round(total_wait_time/n, 1))

# 만약 심사 시간보다 내 도착 시간이 더 길 경우:
#


# 전 사람의 대기 시간 - 내 도착 시간 + 전 사람의 심사 시간 = 내 waitt
#
#
#
# 8
# 0 2
# 10 8
# 7 6
# 1 5
# 8 8
# 4 9
# 7 3
# 2 3

# 전 사람의 대기 시간 - 내 도착 시간 + 전 사람의 심사 시간 = 내 waitt

# 0번: 0분 ~ 2분(심사) 0분
# 1번: 10분~10분(안기다림), 10분~18분(심사) 0분 대기 0분 내도착시간 7분 심사시간 8분 = 1분
# 2번: 17분~18분(기다림), 18분~24분(심사) 1분 대기 1분 내도착시간 1분 심사시간 6분 = 6분
# 3번: 18분~24분(기다림), 24분~29분(심사) 6분
# 4번: 26분~29분(기다림), 29분~37분(심사) 3분
# 5번: 30분~37분(기다림), 37분~46분(심사) 7분
# 6번: 37분~46분(기다림), 46분~49분(심사) 9분
# 7번: 39분~49분(기다림), 49분~52분(심사) 10분
