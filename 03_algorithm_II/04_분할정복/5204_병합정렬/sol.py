import sys
sys.stdin = open('input.txt')
def partition(lst):
    global cnt
    if len(lst) == 1:
        return lst
    else:
        # 인덱스는 이진할때 뭔가 빡세다
        # 그래서 경우를 나눠서 처리
        if len(lst) == 2:
            left = partition(lst[:1])
            right = partition(lst[1:])
        else: 
            left = partition(lst[:len(lst)//2])
            right = partition(lst[len(lst)//2:])
        
        if left[-1] > right[-1]:
            cnt += 1
        left.extend(right)
        result = sorted(left) # 못참음
        return result
    


            

T = int(input())
for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    n_lst = list(map(int,input().split()))
    result = partition(n_lst)
    print(f'#{tc} {result[N//2]} {cnt}')