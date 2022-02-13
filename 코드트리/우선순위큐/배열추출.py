# 배열에 다음과 같은 연산을 할 수 있습니다.

# 1. 배열에 자연수 x를 넣습니다.
# 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거합니다.
# 비어있는 배열에서 시작하여 입력된 연산을 실행하는 프로그램을 작성해보세요.

import heapq

q = []
n = int(input())
for i in range(n):
    a = int(input())
    if a == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-q[0])
            heapq.heappop(q)
    else:
        heapq.heappush(q, -a)