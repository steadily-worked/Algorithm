import heapq
import sys

arvt = []
judgt = []
min_heap = []
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

for i in range(k):
    arvt_idx, judgt_idx = map(int, sys.stdin.readline().split())
    arvt.insert(i, arvt_idx)
    judgt.insert(i, judgt_idx)  # 여기까지 입력값을 리스트로 만드는 과정.
    # ex) 5 / 0 4 / 2 7 / 1 6 / 2 5 / 1 3일 경우
    # arvt = [0, 2, 1, 2, 1], judgt = [4, 7, 6, 5, 3]

total_time_at_immigration = [0 for i in range(k + 1)]  # 심사대에서 총 걸린 시간
pure_wait_time = [0 for i in range(k+1)]  # 우리가 구해야 할 값(각 심사자의 대기시간)
sum_arvt = [0 for i in range(k + 1)]  # 각 심사자의 누적 도착 시간

num = 0
for i in range(len(arvt)):
    if arvt[i] != 0:  # 도착 시간이 0이 아닐 경우에
        num += arvt[i]  # 그 값을 num에 추가하고,
        sum_arvt[i] += num  # 그 num을 sum_arvt[i]에 추가한다.
        # 이 if문이 끝나면 sum_arvt에는 각 참가자별 누적 도착 시간이 들어가게 된다.
for i in range(n):  # 심사대가 n개니까, n명의 사람들은
    heapq.heappush(min_heap, sum_arvt[i] + judgt[i])
    # 우선 대기자가 생기기 전까지는 min_heap에 누적 도착 시간+심사시간 만 넣는다.

for i in range(n, k):
    if sum_arvt[i] >= min_heap[0]:
        # min_heap은 최소힙 처리가 되어있으므로, root 노드인 0번째 인덱스가 제일 작은 값.
        # 그 다음 온 사람의 누적 도착 시간이 그 전 누군가의 누적 도착 시간 + 심사시간(제일 짧음)보다 클 경우,
        # 즉 심사대가 1개 이상 비어있을 경우이다.
        # 그 사람은 대기 시간이 없다.
        total_time_at_immigration[i] = sum_arvt[i] + judgt[i]
        pure_wait_time[i] = 0  # 그래서, 이 심사자의 대기시간은 0분이다.
    else:  # 심사대가 비어있지 않을 경우에는,
        total_time_at_immigration[i] = sum_arvt[i] + \
            abs(sum_arvt[i] - min_heap[0]) + judgt[i]
        # i번째 사람의 대기시간은 (누적 도착 시간 + 심사시간) + 절댓값(도착시간 - 가장 짧은 심사자의 누적도착시간 + 심사시간)
        pure_wait_time[i] = abs(sum_arvt[i] - min_heap[0])
        # 순수 대기 시간은, 본인의 누적 도착 시간에서 가장 짧은 심사자가 총 머문 시간을 뺀 값에 절댓값을 붙인 값이다.
    heapq.heappop(min_heap)  # 이제 가장 짧은 사람은 심사를 마쳤으므로 heapq.heappop을 통해 제거한다.
    # 그리고, i번째 사람이 심사대에 들어가게 되었으므로 heapq.heappush를 통해 추가한다.
    heapq.heappush(min_heap, total_time_at_immigration[i])

print(round(sum(pure_wait_time)/k, 1))  # 순수 대기 시간을 전부 더한 뒤, 소수점 둘째 자리에서 반올림한다.
