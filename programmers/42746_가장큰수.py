# def solution(numbers):
#     numbers = sorted(map(str,numbers),reverse = True)
#     answer = ''
#     for number in numbers:
#         answer += number
#     return answer

from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1  # x가 먼저
    elif x + y < y + x:
        return 1   # y가 먼저
    else:
        return 0   # 같음
# 정렬방식 커스텀 참고
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer = ''.join(numbers)
    return '0' if answer[0] == '0' else answer
