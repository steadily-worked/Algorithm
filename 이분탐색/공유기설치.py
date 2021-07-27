# https://www.acmicpcrhdd.net/problem/2110
import sys
f = sys.stdin.readline

n, c = map(int, f().split())
candidate_list = [int(f()) for _ in range(n)]

candidate_list.sort()

start = 1  # 최저 간격인 1
end = candidate_list[-1] - candidate_list[0]  # 최대간격인 끝집 - 첫집
answer = 0

while start <= end:
    mid = (start + end) // 2  # 간격들의 중간값
    count = 1  # 일단 하나 설치하고 시작. 맨 앞 집에 설치..
    candidate = candidate_list[0]  # 후보지(값 업데이트해주기)
    for i in range(1, n):
        # mid를 더한값보다 더 크다면 공유기 설치해주고 그 위치로 업데이트
        if candidate_list[i] >= candidate + mid:
            count += 1
            candidate = candidate_list[i]
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)
