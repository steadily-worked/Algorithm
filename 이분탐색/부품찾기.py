# 이것이 취업을 위한 코딩 테스트다 with 파이썬 이분탐색 실전문제
import sys
f = sys.stdin.readline

n = int(f())
n_list = list(map(int, f().rstrip().split()))
n_list.sort()
candidate_num = int(f())
candidate_list = list(map(int, f().rstrip().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            print('yes', end=' ')
            return
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print('no', end=' ')
    return


for i in candidate_list:
    binary_search(n_list, i, n_list[0], len(n_list))

# for i in candidate_list:
#     if i in n_list:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
