import sys
a = sys.stdin.readline()

b = list()  # 후보 값 리스트
price = list(map(int, sys.stdin.readline().split()))  # 가격 리스트

price_max = price[0]
price_max_index = 0
price_min = price[0]
price_min_index = 0

for i in range(1, len(price)):
    n = price[i]
    if price_max < n:  # n이 원래의 max값보다 클 경우에는 n을 max값으로 업데이트하고, 인덱스를 i로 업데이트함
        price_max = n
        price_max_index = i
    elif price_min > n:  # n가 원래 min값보다 작을 경우엔 리스트에 기존 값을 담고 다시 돌린다.
        b.append((price_max - price_min, price_max, price_min))
        price_min = n
        price_min_index = i
        price_max = n
        price_max_index = i

b.append((price_max - price_min, price_max, price_min))
# for문이 끝나고 난 뒤의 최대 이익(price_max - price_min)과, 최대값과 최소값을 각각 넣는다.

price_sorted = sorted(b, key=lambda n: (-n[0], n[2]))
# b를, 앞에서부터 이익이 큰 값을 넣고, 이익이 같은 경우 최소값이 낮은 것부터 넣는다.

if price_max_index <= price_min_index:  # 최대값 인덱스가 더 작을 경우. 이럴 땐 최대 이익이 없으므로 -1 출력
    print(-1)
else:
    print(price_sorted[0][1] - price_sorted[0][2])
    print(price_sorted[0][2], price_sorted[0][1])
