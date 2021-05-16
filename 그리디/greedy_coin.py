# input값을 받고 이에 대해 거슬러 준다고 할 때, 필요한 동전의 최소 갯수 구하기

n = int(input())
count = 0

# 큰 단위의 화폐부터 차례로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
