import sys
f = sys.stdin.readline

n, k = map(int, f().split())
a_list = list(map(int, f().split()))
b_list = list(map(int, f().split()))

a_list.sort()
b_list.sort(reverse=True)

# A의 가장 작은 값과 B의 가장 큰 값을 바꿔야한다.

for i in range(k):
    if a_list[i] < b_list[i]:
        a_list[i], b_list[i] = b_list[i], a_list[i]
    else:
        break

print(sum(a_list))
