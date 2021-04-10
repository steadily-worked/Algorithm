a = int(input())
b = list(map(int, input().split()))
b_max = max(b)
b_min = min(b)
if 2 <= a <= 100000:
    for i in range(0, a):
        for j in range(i, len(b)):
            if b[i] == b_min:
                b = b[i:]
            b_max = max(b)
            benefit = b_max - b_min
if benefit > 0:
    print(benefit)
    print(b_min, b_max)
else:
    print(-1)

# 가장 큰 값과 가장 작은 값을 구함
# 이중 for문을 돌면서 i번째 원소가 최솟값일 경우 기존 리스트 시작점을 i번째 인덱스로부터 하도록 하였고(앞 원소들을 버림),
# 그 바뀐 리스트 내에서 다시 b_max로 최대값을 구했음. 그렇게 한 후
# benefit 변수를, 최대값 - 최소값으로 정의함. 이제 for문을 벗어나서
# benefit의 값이 양수인 경우에는 benefit과 최소값, 최대값 을 print했고
# benefit의 값이 음수라면 -1만 print하게 했음
