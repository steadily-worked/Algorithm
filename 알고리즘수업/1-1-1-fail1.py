a = int(input())
b = list(map(int, input().split()))

benefit = 0
b_max = max(b)
if 2 <= a <= 100000:
    for i in range(0, len(b)):
        if b_max == b[-1]:  # 최대값이 맨 뒤에 있을 경우
            benefit += b_max - b[i]  # 기존 benefit 값에 b_max - b[i]한 값을 더해준다.
        else:  # 최대값이 맨 뒤가 아닐 경우
            b_max = max(b[i:])  # 새로운 max값을 i번째 인덱스 이후로 구해준다.
            if b_max == b[i]:  # 최대값이 i번째 값인 경우
                continue  # 그냥 넘어간다.
            else:  # 최대값이 i번째 값이 아닌 경우
                benefit += b_max - b[i]  # 기존 benefit 값에 b_max - b[i]한 값을 더해준다.
print(benefit)


# 알고리즘을 생각해보자.
# 여기서 내가 생각했을 떄 중요한 건.. max값이 어디에 있는가 인 것 같다.
# 그러니까.. 만약 10번째의 값이 가장 크다면, 9번째까지 샀던 걸 전부다 팔면 되니까.
# 만약 max가 가장 뒤에 있다면, 최대 이익은 처음부터 끝까지 max값 - i번째 값 일 것이다.
# max가 맨 뒤에 있는 경우가 아니라면,
# max 전 항까지는 전부 다 산다음 그 때에 파는 게 최대이득일 것이고,
# max 이후 항은 그 다음 max행을 찾아서 똑같은 명령을 주면 될 것 같다.

# 이 알고리즘의 문제점은, 11행에서 다시 한 번 max를 찾기 때문에 시간 복잡도가 증가한다는 것에 있다.
# 시간 복잡도가 O(n^2)가 되었기 때문에 효율적인 알고리즘이 아니다.
