import sys
sys.stdin = open('input.txt')

def midorder(current): #중위 탐색
    if jasik[current][0] != 0:
        midorder(jasik[current][0])
    global count
    count +=1 #중위 탐색 시 순서
    mom[current] = count #완전이진트리에 이진탐색 순서 저장

    if jasik[current][1] != 0:
        midorder(jasik[current][1])


T = int(input())
for tc in range(1,T+1):
    N = int(input()) #노드 개수
    i = 0 # 트리 높이
    while not 2**i-1 < N <= 2**(i+1)-1:
        i += 1
    jasik = [[0,0] for _ in range(2**(i+2))] #자식 노드 개수 인덱스 에러. 시원하게 높이 한 단 더
    rest = N-(2**i-1) #리프노드 개수
    mom = [0]*(N+1) #이진탐색 순서 저장할 리스트
    count = 0
    for c in range(i):
        t = 10e10 #리프노드 개수 체크용. 지장없게 개큰값
        if c == i-1:#막줄
            t = 0
        for cur in range(2**c,2**(c+1)):
            jasik[cur] = [cur*2,cur*2+1]
            t += 2
            if t == rest:#딱일때 아니면 1오바
                break
            elif t - rest == 1:
                jasik[cur][1] = 0
                break



    midorder(1)
    print(f'#{tc} {mom[1]} {mom[N//2]}')





