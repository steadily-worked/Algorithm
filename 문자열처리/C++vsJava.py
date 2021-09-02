# https://www.acmicpc.net/problem/3613
def Java_To_C(v):
    tmp = v[0]
    if tmp.isupper():
        return 'Error!'
    for i in range(1, len(v)):
        if v[i].isupper():
            tmp += '_'
            tmp += v[i].lower()
        else:
            tmp += v[i]

    return tmp


def C_to_Java():
    for i in range(1, len(list(a))):
        if a[i-1] == a[i] == '_':
            return 'Error!'
    if a[0] == '_' or a[-1] == '_':
        return 'Error!'
    a_list = a.split('_')

    for i in a_list:
        if not i.isalnum():
            return 'Error!'
        if i.lower() != i:
            return "Error!"
    for i in range(len(a_list)):
        if a_list[i][0].lower() != a_list[i][0]:
            return 'Error!'
    for i in range(1, len(a_list)):
        a_list[i] = a_list[i].capitalize()
    return ''.join(a_list)


answer_list = []
java_result_list = []

a = input()
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if '_' in a:
    if len(answer_list) == 0:
        answer_list.append(C_to_Java())
else:
    if a.lower() == a:
        print(a)
    else:
        for i in b:
            if i in a:
                if len(answer_list) == 0:
                    answer_list.append(Java_To_C(a))

if len(answer_list) > 0:
    print(''.join(answer_list))
