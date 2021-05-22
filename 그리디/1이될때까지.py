# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 그리디 실전문제 4번 1이 될 때까지
import sys

n, k = map(int, sys.stdin.readline().split())
a = 100000  # 임의의 수
count = 0

for i in range(a):
    if n // k == 0:
        n /= k
        count += 1
        if n != 1:
            continue
        else:
            break
    else:
        n -= 1
        count += 1
        continue

print(count)

# 나눠 떨어지면 n을 k로 나눈 뒤 count를 1 더해주고
#  n이 1이 되면 break, 아니면 continue
# 나눠 떨어지지 않으면 1을 빼주고, count를 1 더해주고 continue

# 5분 걸림
