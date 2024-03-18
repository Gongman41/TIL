# import sys
# sys.stdin = open('input.txt')
def quick(start,end):
    if start >= end:
        return
    pivot =  n_lst[start]
    i = start+1
    j = end 
    # 피벗보다 뒤에 있는 놈들 정렬
    while i <= j:
        #인덱스 에러 안나게
        while i <= end and n_lst[i] <= pivot:
            i += 1
        while j > start and n_lst[j] >= pivot:
            j -= 1
        if i > j: 
            n_lst[start],n_lst[j] = n_lst[j],n_lst[start]
        # 
        else:
            n_lst[i],n_lst[j] = n_lst[j],n_lst[i]
    quick(start, j - 1)
    quick(j+1,end)

# # 파이썬의 장점을 살린 퀵 정렬
# def quick_sort(array):
#     # 리스트가 하나 이하의 원소를 가지면 종료
#     if len(array) <= 1: return array
    
#     pivot, tail = array[0], array[1:]
    
#     leftSide = [x for x in tail if x <= pivot]
#     rightSide = [x for x in tail if x > pivot]
    
#     return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    n_lst = list(map(int,input().split()))
    quick(0,N-1)
    print(n_lst)
    print(f'#{tc} {n_lst[N//2]}')
