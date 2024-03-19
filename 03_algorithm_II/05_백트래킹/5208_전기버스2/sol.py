import sys
sys.stdin = open('input.txt')
def CountSearch(target,cur,energe,cnt):
    global min_cnt
    if cur + energe >= target:
        # 지금 위치랑 연료면 갈 수 있다.
        min_cnt = min(min_cnt,cnt)
        return
    if min_cnt < cnt:
        return
    # 최소값을 넘었다
    
    for i in range(1,energe+1):
        CountSearch(target,cur+i,m_lst[cur+i],cnt+1)
    # 연료 교체하고 다음 위치로 이동

T = int(input())
for tc in range(1,T+1):
    m_lst = list(map(int,input().split()))
    N = m_lst[0]

    min_cnt = 10e10
    CountSearch(N,1,m_lst[1],0)
    print(f'#{tc} {min_cnt}')