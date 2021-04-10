M, e, d, n = map(int, input().split())


def mod(a, b, n):  # a^b mod n을 나타낸 함수입니다.
    result = 1  # result 변수를 선언하고 값 1을 할당합니다.
    while b > 0:  # 지수가 양수인 경우
        if b % 2 != 0:  # 지수가 홀수라면
            # 기존 result 값에 밑 a값을 곱해주고, 그 값을 n으로 나눈 나머지를 result에 할당합니다.
            result = (result * a) % n
        b = b // 2  # b를 2로 나눈 몫을 새롭게 b로 지정합니다.
        a = (a * a) % n  # a를 제곱한 뒤 그 값을 n으로 나눈 나머지를 새롭게 a로 정의합니다.

    return result  # b가 0일 경우 while문을 끝내고 result 값을 할당합니다.


print(mod(M, e, n))
print(mod(mod(M, e, n), d, n))
