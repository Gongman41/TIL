import sys
sys.stdin = open('input.txt')
# 나머지 분배 법칙
# (AxB)%C = (A%C) *(B%C) % C
# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
def make_namuzi(a,num):
    if num == 1:
        return a%C
    else:
        tem = make_namuzi(a,num//2)
        if num%2 == 0:
            return (tem*tem)%C
        else:
            return (tem*tem*a)%C



A,B,C = map(int,input().split())
print(make_namuzi(A,B))
# B만큼 반복하는 게 문제
# if A == 1:
#     if C == 1:
#         print(0)
#     else:
#         print(0)
# else:
#     # C로 나누면 나머지가 0보다 큰 A를 N번 곱한 수.
#     # A를 N번 곱한 수를 M번 곱하기.나머지 더하기.(N*M이 B를 넘어가면 안됨)
#     # 그 과정에서 규칙성 발견?
#     if A < C:
#         N = 0
#         while A*N < C:
#
#             if B <= N:
#                 print(0)
#                 break
#             N += 1
#             # 나머지가 나오는 곱하기 횟수
#         else:


