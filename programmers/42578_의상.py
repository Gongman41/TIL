def solution(clothes):
    # 하나라도 입어야되고, 부위별 최대 한가지
    # 각 부위별 개수 + 1(안썼을때) 랑 다른 쪽이랑 다 곱하고 -1(아무것도 안입었을 때)
    answer = 1
    dict_clothes = {}
    for i in clothes:
        if i[1] in clothes:
            dict_clothes[i[1]].append(i[0])
        else:
            dict_clothes[i[1]] = [i[0]]
    for key in dict_clothes:
        answer *= len(dict_clothes[key])+1
    answer -= 1
    return answer