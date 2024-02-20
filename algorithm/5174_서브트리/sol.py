import sys
sys.stdin = open('input.txt')

def midorder(cur):
    if jasik[cur][0] != 0:
        midorder(jasik[cur][0])
    global count
    count +=1 #서브트리의 노드 개수 카운트

    if jasik[cur][1] != 0:
        midorder(jasik[cur][1])


T = int(input())
for tc in range(1,T+1):
    count = 0
    E,N = map(int,input().split())
    jasik = [[0,0] for _ in range(E+2)] # 1-N까지 노드의 자식저장 리스트
    temp = list(map(int,input().split())) #일단 받기

    for i in range(E):
        for j in range(2):
            if jasik[temp[2*i]][j] == 0:
                jasik[temp[2*i]][j] = temp[2*i+1]
                break # 0일 때 값 하나만 넣고 빠지기. 안그럼 중복
    midorder(N)
    print(f'#{tc} {count}')
    

