# def solution(nums):
#     # 중복이 있는 nums.최대한 다양하게. 중복없게 뽑으면되네.
#     # set 이 해시기반
#     cnt = len(nums)//2
#     set_num = list(set(nums))
#     answer = 0
#     if len(set_num) <= cnt:
#         answer = len(set_num)
#     else:
#         answer = cnt
#     return answer 

def solution(nums):
    cnt = len(nums) // 2
    set_num = set(nums)  # 중복 제거 → 해시
    return min(len(set_num), cnt)
