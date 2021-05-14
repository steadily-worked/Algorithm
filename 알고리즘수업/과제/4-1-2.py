m, n = map(int, input().split())
C = [0] * m
A = [0] * n
for i in range(m-1, -1, -1):
    C[i] = list(map(int, input().split()))

# base case
for a in range(n):
    A[a] = C[0][a]

A_copy = [0] * n

for i in range(1, m):
    if i == 1:  # i가 1인 경우는 C값 만으로 A 값을 업데이트할 수 있음.
        for j in range(n):
            if n == 1:  # 세로로 한 줄 짜리인 경우 그냥 다 더해준다.
                A[j] = C[i][j] + C[i-1][j]
            else:  # n이 2 이상인 경우..
                # 왼쪽 끝이라면 바로 아래 값 / 오른쪽 아래 대각선 값 중 작은 값을 C[i][j]에다가 더해줌.
                if j == 0:
                    A[j] = C[i][j] + min(C[i-1][j], C[i-1][j+1])
                # 오른쪽 끝이라면 바로 아래 값 / 왼쪽 아래 대각선 값 중 작은 값을 C[i][j]에다가 더해줌.
                elif j == n-1:
                    A[j] = C[i][j] + min(C[i-1][j-1], C[i-1][j])
                # 그게 아닐 경우, 왼쪽 아래 대각선 / 바로 아래 / 오른쪽 아래 대각선 값 중 작은 값을 C[i][j]에다가 더해줌
                else:
                    A[j] = C[i][j] + min(C[i-1][j-1], C[i-1][j], C[i-1][j+1])
        A_copy = A.copy()  # i가 2 이상인 경우의 for문에서 바뀌기 전의 A 값을 활용해야 하기 때문에 copy 해줬음
    elif i >= 2:
        for j in range(n):
            if n == 1:  # 세로로 한 줄 짜리인 경우 그냥 다 더해준다.
                A[j] = C[i][j] + A_copy[j]
            else:  # n이 2 이상인 경우..
                # 왼쪽 끝이라면 바로 아래 값 / 오른쪽 아래 대각선 값 중 작은 값을 C[i][j]에다가 더해줌. 여기서, A_copy를 쓰는 이유는 처음에는 그대로 되겠으나 나중에는 바뀐 A의 값을 기준으로 또 A[j]를 정하기 때문에 제대로 된 값이 나올 수가 없기 때문이다.
                if j == 0:
                    A[j] = C[i][j] + min(A_copy[j], A_copy[j+1])
                # 오른쪽 끝이라면 바로 아래 값 / 왼쪽 아래 대각선 값 중 작은 값을 C[i][j]에다가 더해줌.
                elif j == n-1:
                    A[j] = C[i][j] + min(A_copy[j-1], A_copy[j])
                # 그게 아닐 경우, 왼쪽 아래 대각선 / 바로 아래 / 오른쪽 아래 대각선 값 중 작은 값을 C[i][j]에다가 더해줌
                else:
                    A[j] = C[i][j] + min(A_copy[j-1], A_copy[j], A_copy[j+1])
        A_copy = A.copy()  # 매 차례가 끝날 때마다 그 다음 for문에서 A를 구하기 위해 해당 A의 값을 또 copy 해줌
print(min(A))
