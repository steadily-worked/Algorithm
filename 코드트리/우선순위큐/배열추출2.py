# 배열에 다음과 같은 연산을 할 수 있습니다.

# 배열에 정수 x (x ≠ 0) 를 넣습니다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거합니다. ( 절댓값이 가장 작은 값이 여러개일 때는, 그 중 가장 작은 수를 출력하고, 그 값을 배열에서 제거합니다. )
# 비어있는 배열에서 시작하여 입력된 연산을 실행하는 프로그램을 작성해보세요.

import heapq
n = int(input())
q = []

for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(q[0][1])
            heapq.heappop(q)
