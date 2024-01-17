def other_fuc(parm1, parm2):
    result = parm1 * parm2
    print(result, '함수 내부에서 실행')
    return result
answer = other_fuc(2,3)
print(answer, '함수 외부에서 실행')