# # 정렬해서 해당 Xi의 인덱스 값을 출력하면 될듯
# # 근데 그 값의 인덱스를 어떻게
# # 순회하면서 추출된 값에 해당하는 곳에 인덱스 넣기

# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))
# dict = {}
# for n in range(N):
#     if arr[n] in dict:
#         dict[arr[n]].append(n)
#     else:
#         dict[arr[n]] = [n]
# arr.sort()
# result = [-1 for _ in range(N)]
# for num in range(N):
#     for i in dict[arr[num]]:
#         if result[i] == -1:
#             result[i] = num
# print(*result)
    
# dict 에서 배열이 순서가 안맞을 수도
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# (원래 값, 원래 인덱스) 튜플 리스트 생성
sorted_arr = sorted(set(arr))  # 중복 제거 후 정렬
compress_dict = {sorted_arr[i]: i for i in range(len(sorted_arr))}

# 결과 출력
print(*[compress_dict[num] for num in arr])
