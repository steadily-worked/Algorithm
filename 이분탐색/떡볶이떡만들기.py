# 이것이 취업을 위한 코딩 테스트다 with 파이썬 이분탐색 실전문제
import sys
f = sys.stdin.readline

n, m = map(int, f().split())
candidate = sorted(list(map(int, f().split())))

# 중간값을 찾은다음에 기준보다 크면 뺀값만큼 더해주기
result = 0
start = 0
end = candidate[-1]
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in candidate:
        if i > mid:
            total += (i - mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
