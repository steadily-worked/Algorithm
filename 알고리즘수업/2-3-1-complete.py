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

for i in range(0, n-1): # n까지 돌면서
    total_time = sum_list[i] + waitt + judgt[i]
    if sum_list[i+1] >= total_time:
        waitt = 0
    else:
        waitt = total_time - sum_list[i+1]
    total_wait_time += waitt

print(round(total_wait_time/n, 1))
