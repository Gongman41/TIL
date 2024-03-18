import sys
sys.stdin = open('input.txt')
T = int(input())
def ez(start,end,target,switch):
    if start > end:
        return 0
    else:
        middle = (start+end)//2
        if target == n_lst[middle]:
            return 1
        elif target > n_lst[middle] and switch == 'LEFT':
            start= middle +1
            return ez(start,end,target,'RIGHT')
        elif target < n_lst[middle] and switch == 'RIGHT':
            end = middle -1
            return ez(start,end,target,'LEFT')
        else:
            return 0
        
        

for tc in range(1,T+1):
    N,M = map(int,input().split())
    n_lst = sorted(list(map(int,input().split())))
    m_lst = list(map(int,input().split()))
    cnt = 0
    for m in m_lst:
        if ez(0,N-1,m,'LEFT') or ez(0,N-1,m,'RIGHT'):
            cnt += 1

    print(f'{tc} {cnt}')