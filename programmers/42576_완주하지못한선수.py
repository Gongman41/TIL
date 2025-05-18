# def solution(participant, completion):
#     # 양쪽 정렬후 비교하다가 같은 인덱스에 다른 값이 들어가 있을 때 participant에서 출력
#     # 아니면 해시
#     answer = ''
#     if not completion:
#         answer = participant[0]
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant(i) != completion[i]:
#             answer = participant[i]
#     else:
#         answer = participant[-1]
#     return answer

# def solution(participant, completion):
#     hash_dict = {}
#     sum_hash = 0

#     for p in participant:
#         hash_dict[hash(p)] = p
#         sum_hash += hash(p)
    
#     for c in completion:
#         sum_hash -= hash(c)
    
#     return hash_dict[sum_hash]

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
