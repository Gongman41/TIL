def solution(s):
    answer = True
    check_lst = []
    for ss in s:
        if ss == '(':
            check_lst.append(ss)
        else:
            if check_lst and check_lst[-1] == '(':
                check_lst.pop()
            else:
                return False
    if check_lst:
        return False
    return True