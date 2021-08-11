n = int(input())
a_list = [0] * n
for i in range(n):
    a = int(input())
    a_list[i] = a

a_list.sort(reverse=True)
for i in a_list:
    print(i, end=' ')
