import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    n_list = list(map(int,input().split()))
    m_list = list(map(int,input().split()))
    n_list.sort(reverse=True)
    m_list.sort(reverse=True)
    start = 0
    sum_n = 0
    for m in m_list:
        if start == N:
            break
        for n in range(start,N):
            if n_list[n] <= m:
                sum_n += n_list[n]
                start = n+1
                break
    print(f'#{tc} {sum_n}')

