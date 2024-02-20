import sys
sys.stdin = open('input.txt')
T = 10
def midorder(cur):
    if jasik[cur][0] != 0:
        midorder(jasik[cur][0])
    print(mom[cur],end = '')
    if jasik[cur][1] != 0:
        midorder(jasik[cur][1])
    


for tc in range(1,T+1):
    N = int(input())
    jasik = [[0,0] for _ in range(N+1)]
    mom = [0]*(N+1)
    for n in range(1,N+1):
        temp = list(map(str,input().split()))
        if len(temp) == 4: # 인풋이 줄마다 개수가 달라서 따로 처리. 자식노드 바로.
            c,st,l,r = temp
            c,l,r = int(c),int(l),int(r)
            mom[c] = st
            jasik[c] = [l,r]
        elif len(temp) == 3:
            c,st,l = temp
            c,l = int(c),int(l)
            mom[c] = st
            jasik[c] =[l,0]
        else:
            c,st = temp
            c = int(c)
            mom[c] = st
        
    print(f'#{tc} ',end = '')
    midorder(1)
    print()
        

