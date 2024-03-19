import sys
sys.stdin = open('input.txt')
T = int(input())
def peace(n,h,per):
    global max_per
    if h == n:
        max_per = max(max_per,per)
        # max_per = max(max_per,100*per) 하면 값 이상하게 나옴
        return
    elif per <= max_per:
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            peace(n,h+1,per*matrix[h][i]/100)
            visited[i] = 0

# def half_up(num):
#     witch = -1
#     for i in range(len(num)):
#         if num[i] == '.':
#             witch = i + 7
#             break
#     if len(num) < i+7:
#         return float(num)
#     else:
#         if float(num[witch]) >= 5:
#             return float(num[:witch-2]+str(float(num[witch-1])+1))
#         else:
#             return float(num[:witch-1])

for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_per = 0
    visited = [0]*N
    peace(N,0,1)
    max_per = "{:.6f}".format(round(max_per*100,6))
    print(f'#{tc} {max_per}')
