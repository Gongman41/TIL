import sys
sys.stdin = open('input.txt')

def p_making(pp,r):
    if pp < r: # 부모인 애들이 아닐 때
        return mom[r]
    else: #부모임
        if len(mom)-1 == 2*r: # 외동일때
            mom[r] = p_making(pp,2*r)
            return mom[r]
        else:
            mom[r] = p_making(pp,2*r)+p_making(pp,2*r+1)
            return mom[r]
    

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    p = N-M # 리프노드 뺀 애들 개수
    mom = [0]*(N+1)
    for _ in range(M):
        a,b = map(int,input().split())
        mom[a] = b
    p_making(p,1)
    print(f'#{tc} {mom[L]}')


    

