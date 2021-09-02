# https://www.acmicpc.net/problem/2941
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()
for i in croatian:
    if i in a:
        a = a.replace(i, '*')

print(len(a))
