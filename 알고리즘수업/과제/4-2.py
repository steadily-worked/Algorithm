n = int(input())
u, l, star = [0] * n, [0] * n, [0] * n

ud = list(map(int, input().split()))
ld = list(map(int, input().split()))
ul = list(map(int, input().split()))
lu = list(map(int, input().split()))

u[0] = min(ud[0], ld[0] + lu[0])
l[0] = min(ld[0], ud[0] + ul[0])
star[0] = min(u[0] + ud[1], l[0] + ld[1])

ud_last = ud[-1]
ld_last = ld[-1]
for i in range(1, n):
    u[i] = min(u[i-1] + ud[i], l[i-1] + ld[i] + lu[i])
    l[i] = min(l[i-1] + ld[i], u[i-1] + ud[i] + ul[i])
    if u[i] + ud[i+1] > l[i] + ld[i+1]:
        star[i] = l[i] + ld[i+1]
    else:
        star[i] = u[i] + ud[i+1]

print(star[-1])
