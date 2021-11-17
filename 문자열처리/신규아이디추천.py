# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    # 1단계
    first_id = new_id.lower()
    # 2단계
    second_id = re.sub("[^a-z0-9_.-]", "", first_id)
    # 3단계
    second_list = list(second_id)
    third_list = []
    target = '.'
    third_list.append(second_list[0])
    for i in range(1, len(second_list)):
        if second_list[i-1] == target and second_list[i] == target:
            pass
        else:
            third_list.append(second_list[i])
    third_id = ''.join(third_list)
    # 4단계
    if third_id[0] == target:
        third_id = third_id[1:]
    if len(third_id) > 0 and third_id[-1] == target:
        third_id = third_id[:-1]
    fourth_id = third_id
    if len(fourth_id) == 0:
        fourth_id = fourth_id + 'a'
    # 5단계
    fifth_id = fourth_id
    if len(fifth_id) >= 16:
        temp = fifth_id[:15]
        if temp[-1] == '.':
            sixth_id = temp[:-1]
        else:
            sixth_id = temp
    else:
        sixth_id = fifth_id
    if len(sixth_id) <= 2:
        while len(sixth_id) < 3:
            sixth_id += sixth_id[-1]
    answer = sixth_id
    return answer