# https://www.acmicpc.net/problem/14405
p_list = ['pi', 'ka', 'chu']

a = input()
for i in p_list:
    if i in a:
        a = a.replace(i, '*')

flag = True
for i in a:
    if i != '*':
        flag = False
    else:
        continue
if flag:
    print("YES")
else:
    print("NO")
