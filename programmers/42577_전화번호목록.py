# def solution(phone_book):
#     phone_book.sort()
#     answer = True

#     for i in range(len(phone_book)-1):
#         if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
#             answer = False
#             break
#     return answer

def solution(phone_book):
    phone_dict = {}
    for number in phone_book:
        phone_dict[number] = True  # 전화번호 해시 테이블에 저장

    for number in phone_book:
        temp = ""
        for ch in number[:-1]:  # 자기 자신은 제외하고 앞부분들만 탐색
            temp += ch
            if temp in phone_dict:
                return False
    return True
# 딕셔너리 만든다음 자기자신제외(넣으면 무조건 나오니까)하고 접두어있나 확인.