# # 번갈아서 가는거랑 가운데 하나 건너뛰고 반대편가는거.
# # 50 40 200 140 
# # 30 100 120 210
# import sys
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     lst = []
#     tem_lst = [[0]*n for _ in range(2)]
#     for _ in range(2):
#         lst.append(list(map(int,input().split())))
#     tem_lst[0][0],tem_lst[1][0] = lst[0][0], lst[1][0]
#     for i in range(n-2):
#         tem_lst[1][i+1] = max(tem_lst[1][i+1], tem_lst[0][i] + lst[1][i+1])
#         tem_lst[0][i+1] = max(tem_lst[0][i+1],tem_lst[1][i] + lst[0][i+1])
#         tem_lst[1][i+2] = max(tem_lst[1][i+2],max(tem_lst[0][i+1], tem_lst[0][i]) + lst[1][i+2])
#         tem_lst[0][i+2] = max(tem_lst[0][i+2],max(tem_lst[1][i+1], tem_lst[1][i]) + lst[0][i+2])
#     print(max(tem_lst[0][n-1],tem_lst[1][n-1]))

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(lst[0][0], lst[1][0]))
        continue

    # DP 테이블 초기화
    lst[0][1] += lst[1][0]
    lst[1][1] += lst[0][0]

    # DP 진행 (Bottom-up)
    for i in range(2, n):
        lst[0][i] += max(lst[1][i-1], lst[1][i-2])
        lst[1][i] += max(lst[0][i-1], lst[0][i-2])

    # 최대값 출력
    print(max(lst[0][n-1], lst[1][n-1]))
