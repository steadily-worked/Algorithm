m, n = map(int, input().split())
C = [0] * m
A = [0] * n
A_copy = [0] * n
for i in range(m-1, -1, -1):
    C[i] = list(map(int, input().split()))  # C[i]의 값은 input 받아서 그대로 넣기

# base case
for a in range(n):
    if a == 0:
        A[a] = C[0][a]  # a가 0이면 C의 값 그대로 가져오기
    else:
        A[a] = A[a-1] + C[0][a]  # 0이 아니면 왼쪽 값에서 C의 값을 더해주기
    A_copy = A.copy()  # 해당 값을 복사함. 기존에 있던 A의 값이, 바뀔 A의 값을 결정하기 때문

for i in range(1, m):
    for j in range(n):
        if n == 1:  # 세로로 한 줄인 경우
            A[j] += C[i][j]  # 그냥 기존 A의 값에서 C의 값을 더해주는 방식으로 다 더해줌
        else:
            if j == 0:  # j가 0일 경우
                A[j] = A[j] + C[i][j]  # 위에처럼 기존 A의 값에서 해당하는 C의 인덱스 값을 더해준다.
            else:
                # C의 값에다가 (A[j] 기준 왼쪽 값과, 바뀌기 전 A_copy의 j번째 인덱스 값 중 더 작은 값을 더해준다.
                A[j] = C[i][j] + min(A[j-1], A_copy[j])
        A_copy = A.copy()  # 한 번의 for문이 끝날 때마다 완성된 A의 값을 그대로 복사하여 A_copy에 부여한다.
print(A[-1])  # 완성된 A의 배열의 가장 마지막 값, 그러니까 (m, n)의 값을 출력한다.
