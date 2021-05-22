# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 그리디 실전문제 2번 큰수의 법칙

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(1, m+1):
    if i // k != 0:
        ans += max(a)
    else:
        a.sort()
        ans += a[-2]

print(ans)

# 풀이 15분 걸림

# 좀더 효율적인 버전

# n, m, k, a 구하는 과정은 동일

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count * first)  # 가장 큰 수 더하기
result += (m-count) * second  # 두 번째로 큰 수 더하기

print(result)  # 최종 답안 출력
