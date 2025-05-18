# def solution(citations):
#     citations.sort()
#     cit_len = len(citations)
#     answer = 0
#     for i in range(cit_len):
#         if cit_len - i < citations[i]:
#             break
#         answer = citations[i]
            
#     return answer

def solution(citations):
    citations.sort()
    n = len(citations)

    for i in range(n):
        h = n - i
        if citations[i] >= h:
            return h
    return 0
