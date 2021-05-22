# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 그리디 유형별 기출문제 2 곱하기 혹은 더하기

a = input()
b = list(map(int, list(str(a))))

result = b[0]

for i in range(1, len(b)):
    if b[i] != 0:
        if result != 0:
            result *= b[i]
        else:
            result += b[i]

print(result)
