# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 그리디 유형별 기출문제 1 모험가 길드

n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    if a.count(i) >= i:
        count += 1
    else:
        continue

print(count)

# 8분 걸림
