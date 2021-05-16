arvt = []
judgt = []
k = int(input())

for i in range(k):
    arvt_idx, judgt_idx = map(int, input().split())
    arvt.insert(i, arvt_idx)
    judgt.insert(i, judgt_idx)

waitt = [0 for i in range(k + 1)]
pure_wait_time = [0 for i in range(k+1)]
sum_arvt = [0 for i in range(k + 1)]

num = 0
for i in range(len(arvt)):
    if arvt[i] != 0:
        num += arvt[i]
    sum_arvt[i] += num

k1 = sum_arvt[0] + judgt[0]
k2 = sum_arvt[1] + judgt[1]

for i in range(2, k):
    waitt[i] = sum_arvt[i] + \
        min(abs(sum_arvt[i] - k1), abs(sum_arvt[i] - k2)) + judgt[i]
    pure_wait_time[i] = min(abs(sum_arvt[i] - k1), abs(sum_arvt[i] - k2))
    if k1 > k2:
        k2 = waitt[i]
    else:
        k1 = waitt[i]

print(round(sum(pure_wait_time)/k, 1))
