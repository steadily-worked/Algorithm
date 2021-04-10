n = int(input())
num_list = list(map(int, input().split()))
K = int(input())


def binary_search(n, num_list, K):
    num_list.sort()
    left = 0
    right = len(num_list) - 1
    while left <= right:
        if 2 <= n <= 100000:
            mid = (left + right) // 2
            if K == num_list[mid]:
                return num_list[mid]
            elif K < num_list[mid]:
                right = mid - 1
            else:
                left = mid + 1

    if K not in num_list:
        low = abs(K - num_list[left])
        high = abs(num_list[right] - K)

        result = num_list[left] if low <= high else num_list[right]

        return result


print(binary_search(n, num_list, K))

# 같은 값이 여러개라면, 이들 중 작은 수를 출력하기.

# 13
# 20 30 40 55 60 70 75 80 85 90 91 93 100
# 92

# mid = 75
# K가 75보다 크니까, 이제 left가 7이 됨
# 새로운 배열: [75, 80, 85, 90, 91, 93, 100]


# binary search로 내가 원하는 값이 배열 안에 있는지 찾다가,
# 있다면 그걸 리턴하고
# 없다면 low값과 high값 중에서 어느 것이 obj, 원하는 값과의 차가 작은지 비교해서
# 더 근접한 값을 리턴한다.
